from django.shortcuts import render

def home(request):
    return render(request, 'sample_app/home.html',{})

def about(request):
    return render(request, 'sample_app/about.html',{})

def help(request):
    return render(request, 'sample_app/help.html',{})
