import os
import django
import requests

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CardGame.settings')
django.setup()
from faker import Faker
from django.contrib.auth.models import User
from accounts.models import Profile, TypeProfile
from trading.models import Card, Deck, Transaction
import random

f = Faker()

def populate_profile_type():
    types = ['beginner', 'gold', 'expert', 'ninja']
    for type in types:
        profile_type = TypeProfile.objects.create(name=type)

def populate_user(num):
    for i in range(num):
        fname = f.first_name()
        lname = f.last_name()
        username = fname.lower() + lname.lower()
        email = f.email()
        password = 'Sailboat12'
        user = User.objects.create_user(username=username, password=password, first_name=fname, last_name=lname, email=email)


# for user in User.objects.filter(profile__isnull=True):
#     Profile.objects.create(user=user)



def populate_card(number):
    for i in range(1,number):
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{i}/')
        if response.status_code == 200:
            data = response.json()
            id = data['id']
            name = data['name']
            image = data['sprites']['other']['home']['front_default']

            resp = requests.get(data['species']['url'])
            data2 = resp.json()
            if response.status_code == 200:
                rarity = data2['capture_rate']
            else:
                rarity = 0

            card = Card.objects.create(card_id=id, name=name, rarity=rarity, image=image)
