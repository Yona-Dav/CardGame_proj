from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import Profile, User
import random
from trading.models import Card, Deck

@receiver(post_save, sender=User)
def my_callback(sender, instance, created, **kwargs):
    if created:
        prof = Profile.objects.create(user=instance)

        cards = Card.objects.all().order_by('rarity')
        num = cards.count() / 10
        decks = random.sample(list(cards[0:num]), k=1) + random.sample(list(cards[num:num * 3]), k=3) + random.sample(list(cards[num * 3:num * 6]), k=15) + random.sample(list(cards[num * 6:num * 10]), k=30)

        deck = Deck.objects.create(user=prof)
        deck.card.add(*decks)