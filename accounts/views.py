from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, ListView, View, DeleteView
from django.contrib.auth.views import LoginView
from .models import User, Profile
from .forms import SignupForm, MyAuthenticationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

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


class ProfileViewList(ListView, UserPassesTestMixin):
    model = Profile
    template_name = 'profile_list.html'
    context_object_name = 'profiles'

    def test_func(self):
        return self.request.user.is_staff


class DeleteProfile(DeleteView, UserPassesTestMixin):
    model = Profile
    template_name = 'delete_view.html'
    success_url = reverse_lazy('all_profiles')
    success_message = "The profile was deleted successfully"

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message  % obj.__dict__)
        return super(DeleteProfile, self).delete(request, *args, **kwargs)


class UserViewList(ListView, UserPassesTestMixin):
    model = User
    template_name = 'user_list.html'
    context_object_name = 'users'

    def test_func(self):
        return self.request.user.is_staff


class DeleteUser(DeleteView, UserPassesTestMixin):
    model = User
    template_name = 'delete_view.html'
    success_url = reverse_lazy('all_users')
    success_message = "The user was deleted successfully"

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message  % obj.__dict__)
        return super(DeleteUser, self).delete(request, *args, **kwargs)

    def test_func(self):
        return self.request.user.is_staff