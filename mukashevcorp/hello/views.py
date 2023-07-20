from django.apps import apps
from django.shortcuts import render
from django.views.generic.base import TemplateView


# Create your views here.


def index(request):
    app_configs = apps.get_app_configs()
    modules = []

    for app_config in app_configs:
        if 'django' not in app_config.name:
            modules.append(app_config)

    context = {
        'modules': modules[2:],
        'start': True
    }
    return render(request, 'hello/index.html', context)


def hello(request):
    context = {
        'start': False
    }
    return render(request, 'hello/index.html', context)
