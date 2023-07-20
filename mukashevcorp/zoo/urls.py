from django.urls import path
from . import views

app_name = 'zoo'

urlpatterns = [
    path('', views.index)
]
