from django.urls import path
from . import views

urlpatterns = [
    path('homepage/', views.homepage, name='homepage'),
    path('allCards/', views.CardListView.as_view(), name='all_cards'),
    path('myDeck/', views.MyCardListView.as_view(), name='my_deck'),
    path('transactions/', views.TransactionView.as_view(), name='transactions'),
    path('transactions/<int:card_id>/', views.start_transaction, name='start_transaction'),
    path('transactions/remove/<int:transaction_id>/', views.remove_my_transaction, name='remove_transaction'),
    path('transactions/makeOffer/<int:transaction_id>/', views.OfferCreateView.as_view(), name='new_offer'),
    path('transactions/viewOffer/<int:pk>/', views.OfferView.as_view(), name='all_offers'),
    path('transactions/viewOffer/<int:offer_id>/<int:accepted>', views.transaction_action, name='action'),
    path('<int:pk>/deleteCard/', views.DeleteCard.as_view(), name='delete_card'),
    path('allCards/newCard/', views.CardCreateView.as_view(), name='new_card')
]