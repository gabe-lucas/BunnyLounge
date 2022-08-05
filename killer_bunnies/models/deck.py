from django.db import models

from .card import Card

class Deck(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    color = models.CharField(max_length=7)
    poster = models.ImageField(upload_to='decks', blank=True)
    cards = models.ManyToManyField(Card, blank=True)

    def __str__(self):
        return self.name