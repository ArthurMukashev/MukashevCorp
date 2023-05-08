from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'start': True
    }
    return render(request, 'hello/index.html', context)

def hello(request):
    context = {
        'start': False
    }
    return render(request, 'hello/index.html', context)
