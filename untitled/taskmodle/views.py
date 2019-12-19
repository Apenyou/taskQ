from django.shortcuts import render

# Create your views here.

def hello(request):
    context          = {}
    context['hello'] = ''
    return render(request, 'test.html', context)
