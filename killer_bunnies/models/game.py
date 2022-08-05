from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    decks = models.ManyToManyField('Deck', blank=True)
    poster = models.ImageField(upload_to='games', blank=True)

    def __str__(self):
        return self.name
