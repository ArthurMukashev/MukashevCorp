from django.views import generic
from django.urls import reverse_lazy

from .models import ReportFragment
from .services import generate_pdf


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'reports/index.html'
    context_object_name = 'ReportFragments'

    def get_queryset(self):
        pass
        # return ReportFragment.objects.values('report_year')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        years = ReportFragment.objects.values('report_year')
        years = [*set(map(lambda x: x['report_year'], years))]
        context['years'] = years
        return context


class TotalView(generic.ListView):
    model = ReportFragment
    context_object_name = 'ReportFragments'
    template_name = 'reports/total.html'

    def get_queryset(self):
        year = self.kwargs.get('year', None)
        return ReportFragment.objects.filter(report_year=year)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TotalView, self).get_context_data(**kwargs)
        year = self.kwargs.get('year', None)
        context['year'] = year
        return context


def download_generated_pdf(request, year):
    return generate_pdf.getpdf(request, year)


class ManageView(generic.ListView):
    template_name = 'reports/manage.html'
    context_object_name = 'ReportFragments'

    def get_queryset(self):
        return ReportFragment.objects.filter(author=self.request.user)


class ReportCreateView(generic.CreateView):
    model = ReportFragment
    fields = ['report_name', 'report_year', 'report_order', 'report_text']
    template_name = 'reports/add.html'

    success_url = reverse_lazy('reports:manage')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ReportDeleteView(generic.DeleteView):
    model = ReportFragment
    template_name = 'reports/confirm_delete.html'
    success_url = reverse_lazy('reports:manage')


class ReportUpdateView(generic.UpdateView):
    model = ReportFragment
    fields = ['report_name', 'report_year', 'report_order', 'report_text']
    template_name = 'reports/add.html'
    success_url = reverse_lazy('reports:manage')
