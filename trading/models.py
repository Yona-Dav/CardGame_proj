from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import Profile, User
from django.db import models
from django.conf import settings

import random


class Card(models.Model):
    card_id = models.PositiveIntegerField()
    name = models.CharField(max_length=50)
    rarity = models.PositiveIntegerField(default=0)
    image = models.URLField()


    def __str__(self):
        return self.name


class Deck(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    card = models.ManyToManyField(Card, related_name='deck')


class Transaction(models.Model):
    STATUS = [('S', 'Start'), ('E', 'End')]
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    user_sell = models.ForeignKey(Profile, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS, default='S', max_length=30)



@receiver(post_save, sender=User)
def my_callback(sender, instance, created, **kwargs):
    if created:
        prof = Profile.objects.create(user=instance)

        cards = Card.objects.all().order_by('rarity')
        num = cards.count() / 10
        decks = random.sample(list(cards[0:num]), k=1) + random.sample(list(cards[num:num * 3]), k=3) + random.sample(list(cards[num * 3:num * 6]), k=15) + random.sample(list(cards[num * 6:num * 10]), k=30)

        deck = Deck.objects.create(user=prof)
        deck.card.add(*decks)






