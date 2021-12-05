from django.urls import path
from . import views

urlpatterns = [
    path('homepage/', views.homepage, name='homepage'),
    path('allCards/', views.CardListView.as_view(), name='all_cards'),
]