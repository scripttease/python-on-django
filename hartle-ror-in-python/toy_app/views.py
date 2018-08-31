from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from .forms import UserForm
from django.shortcuts import redirect

def hello(request):
    return render(request, 'toy_app/hello.html', {})

def user_list(request):

    users = User.objects.all
    # Note that the variable in brackets is passed to the template so we can use 'users' in the template. This is like @variables in Rails
    return render(request, 'toy_app/user_list.html', {'users': users})

def user_show(request, pk):
    user = get_object_or_404(User, pk=pk) 

    return render(request, 'toy_app/user_show.html', {'user': user})

def user_new(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.date_joined = timezone.now()
            user.save()
            return redirect('user_show', pk=user.pk)
    else:
        form = UserForm()
    return render(request, 'toy_app/user_edit.html', {'form': form})

def user_edit(request, pk):
    user = get_object_or_404(User, pk=pk) 
    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.daye_joined = timezone.now()
            user.save()
            return redirect('user_show', pk=user.pk)
    else:
        form = UserForm(instance=user)
    return render(request, 'toy_app/user_edit.html', {'form': form})


