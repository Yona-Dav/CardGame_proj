from django import forms
from .models import *


class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = ['card']


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = '__all__'