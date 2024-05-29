from django.db import models


class Author(models.Model):
    name = models.TextField(null=False, blank=False)


class Genre(models.Model):
    name = models.TextField(null=False, blank=False)


class Book(models.Model):
    title = models.TextField(null=False, blank=True)
    author = models.ForeignKey('Author', related_name='books', on_delete=models.CASCADE)
    genre = models.ForeignKey('Genre', related_name='books', on_delete=models.CASCADE)