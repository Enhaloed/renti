import json
import re

from book_club.models import Book, Author, Genre

from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = 'imports book_club/static/books/books.json'

    def handle(selfself, *args, **kwargs):
        with open('book_club/static/books/books.json', encoding='utf-8') as json_file:
            data = json.load(json_file)
            for book in data:
                author, created = Author.objects.get_or_create(name=book['author'])
                genre, created = Genre.objects.get_or_create(name=book['genre'])
                Book.objects.get_or_create(
                    title=book['title'],
                    author=author,
                    genre=genre,
                )