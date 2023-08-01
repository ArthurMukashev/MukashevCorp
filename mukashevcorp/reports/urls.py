from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'reports'

urlpatterns = [
    path('', login_required(views.IndexView.as_view()), name='index'),
    path('manage/', login_required(views.ManageView.as_view()), name='manage'),
    path('manage/add/', login_required(views.ReportCreateView.as_view()), name='add'),
    path('manage/<int:pk>/', login_required(views.ReportUpdateView.as_view()), name='update'),
    path('manage/<int:pk>/delete/', login_required(views.ReportDeleteView.as_view()), name='delete'),

    path('total/<int:year>/', views.TotalView.as_view(), name='total'),
]
