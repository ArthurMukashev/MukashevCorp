from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.urls import reverse_lazy

from .forms import InformationSchemaForm
from .models import AccessMatrix, InformationSchema


# Create your views here.

class IndexView(generic.ListView):
    template_name = 'diagram_editor/index.html'
    context_object_name = 'schemes'

    def get_queryset(self):
        return InformationSchema.objects.all()


def information_schema_create(request):
    if request.method == 'POST':
        form = InformationSchemaForm(request.POST)
        print(request.POST)
        return
        if form.is_valid():
            form.instance.author = request.user
            form.save()
        return HttpResponseRedirect(reverse_lazy('diagram_editor:index'))
    else:
        form = InformationSchemaForm()
    return render(request, 'diagram_editor/new.html', {'form': form})


def information_schema_update(request, pk):
    if request.method == 'POST':
        form = InformationSchemaForm(request.POST)
    else:
        schema = get_object_or_404(InformationSchema, pk=pk)
        print(schema.desc_short)
        form = InformationSchemaForm(initial={})
    return render(request, 'diagram_editor/new.html', {'form': form})


class InformationSchemaEditView(generic.UpdateView):
    model = InformationSchema
    fields = ['name', 'desc_short', 'description', 'linked', 'permitted_groups']
    template_name = 'diagram_editor/new.html'
    success_url = reverse_lazy('diagram_editor:index')
