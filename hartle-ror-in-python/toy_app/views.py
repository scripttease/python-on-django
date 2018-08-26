from django.shortcuts import render

def hello(request):
    return render(request, 'toy_app/hello.html', {})
