from django.urls import path
from . import views

app_name = 'diagram_editor'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('new/', views.InformationSchemaCreateView.as_view(), name='new'),
    path('edit/<int:pk>/', views.InformationSchemaEditView.as_view(), name='edit')
]
