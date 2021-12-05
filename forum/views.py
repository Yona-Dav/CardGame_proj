from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DetailView, ListView, View, DeleteView
from .models import Thread, Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import ThreadForm
from django.http import HttpResponseRedirect
# Create your views here.


class ForumListView(ListView):
    model = Thread
    template_name = 'forum.html'
    context_object_name = 'threads'


class ThreadCreateView(LoginRequiredMixin, CreateView):
    model = Thread
    form_class = ThreadForm
    success_url = reverse_lazy('forum')
    template_name = 'new_thread.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.creator = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get(self,  request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['content']
    template_name = 'new_comment.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.creator = self.request.user
        thread_id = self.kwargs['thread_id']
        thread = Thread.objects.get(id=thread_id)
        self.object.thread = thread
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('forum')


class ThreadDetailView(DetailView):
    model = Thread
    template_name = 'view_thread.html'


