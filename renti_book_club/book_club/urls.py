from django.urls import path
from django.shortcuts import redirect

from . import views

urlpatterns = [
    path('', lambda req: redirect('/search/'), name='cardDatabase-home'),
    path('search/', views.search_for_books, name='book_club_search'),
]