from django.shortcuts import render, redirect
from .models import Card, Transaction, Deck, Offer
from django.views.generic import CreateView, UpdateView, DetailView, ListView, View, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import OfferForm, CardForm
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages


# Create your views here.

def homepage(request):
    return render(request, 'homepage.html')

class CardListView(ListView):
    model = Card
    template_name = 'all_cards.html'
    context_object_name = 'cards'


class MyCardListView(LoginRequiredMixin,ListView):
    model = Card
    template_name = 'my_deck.html'


class TransactionView(ListView, LoginRequiredMixin):
    model = Transaction
    template_name = 'transactions.html'
    context_object_name = 'transactions'

    def get_queryset(self):
        return super(TransactionView, self).get_queryset().filter(status='S')


@login_required
def start_transaction(request, card_id):
    new_transaction = Transaction.objects.create(card=Card.objects.get(id=card_id), user_sell=request.user.profile, status='S')
    deck = Deck.objects.get(user=request.user.profile)
    deck.card.remove(Card.objects.get(id=card_id))
    return redirect('transactions')


@login_required
def remove_my_transaction(request, transaction_id):
    transaction = Transaction.objects.get(id=transaction_id)
    transaction.status = 'E'
    transaction.save()
    deck = Deck.objects.get(user=request.user.profile)
    deck.card.add(transaction.card)
    return redirect('transactions')


class OfferCreateView(LoginRequiredMixin, CreateView):
    template_name = 'new_offer.html'
    success_url = reverse_lazy('transactions')
    model = Offer
    form_class = OfferForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        if self.object.card in self.request.user.profile.deck.card.all():
            self.object.buyer = self.request.user.profile
            transaction_id = self.kwargs['transaction_id']
            transaction = Transaction.objects.get(id=transaction_id)
            self.object.transaction = transaction
            self.object = form.save()
            return HttpResponseRedirect(self.get_success_url())
        return render(self.request, 'not_have.html')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['card'].queryset = self.request.user.profile.deck.card.all()
        return form



class OfferView(LoginRequiredMixin, DetailView):
    model = Transaction
    template_name = 'all_offers.html'
    context = Offer

@login_required
def transaction_action(request, offer_id, accepted):
    offer = Offer.objects.get(id=offer_id)
    transaction = offer.transaction
    deck_seller = Deck.objects.get(user=transaction.user_sell)
    deck_buyer = Deck.objects.get(user=offer.buyer)
    if accepted:
        offer.status = 'A'
        transaction.status = 'E'
        offer.save()
        transaction.save()
        deck_buyer.card.add(transaction.card)
        deck_seller.card.add(offer.card)
        deck_buyer.card.remove(offer.card)
        return redirect('transactions')
    else:
        offer.status = 'R'
        offer.save()
        return redirect('all_offers', transaction.id)


class DeleteCard(DeleteView, UserPassesTestMixin):
    model = Card
    template_name = 'delete_view.html'
    success_url = reverse_lazy('all_cards')
    success_message = "The card was deleted successfully"

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message  % obj.__dict__)
        return super(DeleteCard, self).delete(request, *args, **kwargs)

    def test_func(self):
        return self.request.user.is_staff


class CardCreateView(CreateView, UserPassesTestMixin):
    template_name = 'new_card.html'
    success_url = reverse_lazy('all_cards')
    model = Card
    form_class = CardForm

    def form_valid(self, form):
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())

    def test_func(self):
        return self.request.user.is_staff