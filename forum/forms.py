from django.contrib.auth.models import User
from django import forms
from .models import Comment, Thread

class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        exclude = ['creator']
