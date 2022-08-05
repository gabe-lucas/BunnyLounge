from django.db import models

class Bunnybit(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)