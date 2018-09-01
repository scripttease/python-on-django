from django.db import models
from django import forms
from django.contrib.auth.models import User
from .models import Micropost


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        # fields = ('first_name', 'last_name', 'email', 'password',)
        fields = ('first_name', 'last_name', 'email',)


class MicropostForm(forms.ModelForm):

    class Meta:
        model = Micropost
        fields = ('title','content',)
