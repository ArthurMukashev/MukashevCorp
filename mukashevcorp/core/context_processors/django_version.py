import django


def django_version(request):
    return {'django_version': '.'.join(map(str, django.VERSION[:3]))}
