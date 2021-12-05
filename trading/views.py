from django.shortcuts import render
from .models import Card, Transaction
from django.views.generic import CreateView, UpdateView, DetailView, ListView, View, DeleteView


# Create your views here.

def homepage(request):
    return render(request, 'homepage.html')

class CardListView(ListView):
    model = Card
    template_name = 'all_cards.html'
    context_object_name = 'cards'

