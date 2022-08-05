from django.db import models

class DieTypes(models.TextChoices):
    D7 = 'D7', 'D7'
    D10 = 'D10', 'D10'
    D12 = 'D12', 'D12'
    D20 = 'D20', 'D20'
    ZODIAC = 'ZODIAC', 'Zodiac'
    CHINESE_ZODIAC = 'CHINESE_ZODIAC', 'Chinese Zodiac'

class Die(models.Model):
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=255, choices=DieTypes.choices)
    color = models.CharField(max_length=7)