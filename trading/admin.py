from django.contrib import admin

# Register your models here.

from trading.models import Deck, Card,Transaction
admin.site.register(Card)
admin.site.register(Transaction)
admin.site.register(Deck)
