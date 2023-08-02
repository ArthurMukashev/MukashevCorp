from django.urls import path
from . import views

app_name = 'diagram_editor'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # path('new/', views.InformationSchemaCreateView.as_view(), name='new'),
    path('new/', views.information_schema_create, name='new'),
    path('edit/<int:pk>/', views.information_schema_update, name='edit')
]
