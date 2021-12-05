from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, ListView, View, DeleteView
from django.contrib.auth.views import LoginView
from .models import User, Profile
from .forms import SignupForm, MyAuthenticationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.


class Signup(CreateView):
    model = User
    form_class = SignupForm
    success_url = reverse_lazy('update_profile')
    template_name = 'signup.html'

    def form_valid(self, form):
        self.object = form.save()
        user = authenticate(self.request, username=self.object.username, password=form.cleaned_data['password1'])
        if user:
            login(self.request, user)
        return HttpResponseRedirect(self.get_success_url())


class UpdateProfile(UpdateView):
    model = Profile
    fields = ['image']
    success_url = reverse_lazy('homepage')
    template_name = 'update_profile.html'

    def get_object(self, queryset=None):
        return self.request.user.profile


class MyLoginView(LoginView):
    template_name = 'login.html'
    form_class = MyAuthenticationForm


class ViewProfile(DetailView):
    model = User
    template_name = 'profile.html'




