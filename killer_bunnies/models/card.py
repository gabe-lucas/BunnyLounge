from django.db import models
from .die import Die

class CardType(models.TextChoices):
    RUN = 'RUN', 'Run'
    SPECIAL = 'SPECIAL', 'Special'
    VERY_SPECIAL = 'VERY_SPECIAL', 'Very Special'
    BUNDERGROUND_STATION = 'BUNDERGROUND_STATION', 'Bunderground Station'
    CARROT_SUPPLY = 'CARROT_SUPPLY', 'Carrot Supply'
    CHINESE_ZODIAC = 'CHINESE_ZODIAC', 'Chinese Zodiac'
    DOLLA = 'DOLLA', 'Dolla'
    METAL = 'METAL', 'Metal'
    MYSTERIOUS_PLACE = 'MYSTERIOUS_PLACE', 'Mysterious Place'
    PLAY_IMMEDIATELY = 'PLAY_IMMEDIATELY', 'Play Immediately'
    RANK = 'RANK', 'Rank'
    ROAMING_RED_RUN = 'ROAMING_RED_RUN', 'Roaming Red'
    ZODIAC = 'ZODIAC', 'Zodiac'

class Rank(models.TextChoices):
    OFFICER_1 = 'O1', 'Officer 1'
    OFFICER_2 = 'O2', 'Officer 2'
    OFFICER_3 = 'O3', 'Officer 3'
    OFFICER_4 = 'O4', 'Officer 4'
    OFFICER_5 = 'O5', 'Officer 5'
    OFFICER_6 = 'O6', 'Officer 6'
    OFFICER_7 = 'O7', 'Officer 7'
    OFFICER_8 = 'O8', 'Officer 8'
    OFFICER_9 = 'O9', 'Officer 9'

    ENLISTED_1 = 'E1', 'Enlisted 1'
    ENLISTED_2 = 'E2', 'Enlisted 2'
    ENLISTED_3 = 'E3', 'Enlisted 3'
    ENLISTED_4 = 'E4', 'Enlisted 4'
    ENLISTED_5 = 'E5', 'Enlisted 5'
    ENLISTED_6 = 'E6', 'Enlisted 6'
    ENLISTED_7 = 'E7', 'Enlisted 7'
    ENLISTED_8 = 'E8', 'Enlisted 8'
    ENLISTED_9 = 'E9', 'Enlisted 9'

class ZodiacSign(models.TextChoices):
    AQUARIUS = 'AQUARIUS', 'Aquarius'
    ARIES = 'ARIES', 'Aries'
    CANCER = 'CANCER', 'Cancer'
    CAPRICORN = 'CAPRICORN', 'Capricorn'
    GEMINI = 'GEMINI', 'Gemini'
    LEO = 'LEO', 'Leo'
    LIBRA = 'LIBRA', 'Libra'
    PISCES = 'PISCES', 'Pisces'
    SAGITTARIUS = 'SAGITTARIUS', 'Sagittarius'
    SCORPIO = 'SCORPIO', 'Scorpio'
    TAURUS = 'TAURUS', 'Taurus'
    VIRGO = 'VIRGO', 'Virgo'

class ZodiacAnimal(models.TextChoices):
    DOG = 'DOG', 'Dog'
    DRAGON = 'DRAGON', 'Dragon'
    GOAT = 'GOAT', 'Goat'
    HORSE = 'HORSE', 'Horse'
    MONKEY = 'MONKEY', 'Monkey'
    OX = 'OX', 'Ox'
    PIG = 'PIG', 'Pig'
    RABBIT = 'RABBIT', 'Rabbit'
    RAT = 'RAT', 'Rat'
    ROOSTER = 'ROOSTER', 'Rooster'
    SNAKE = 'SNAKE', 'Snake'
    TIGER = 'TIGER', 'Tiger'

class BunnyRequirement(models.TextChoices):
    PLAY_X2 = 'PLAY_X2', 'Play X2'
    PLAY_AND_SAVE = 'PLAY_AND_SAVE', 'Play and Save'
    PLAY = 'PLAY', 'Play'
    NO = 'NO', 'No'

class Pawn(models.TextChoices):
    WHITE = 'WHITE', 'White'
    BLACK = 'BLACK', 'Black'
    RED = 'RED', 'Red'
    GREEN = 'GREEN', 'Green'
    BLUE = 'BLUE', 'Blue'
    YELLOW = 'YELLOW', 'Yellow'
    VIOLET = 'VIOLET', 'Violet'
    PINK = 'PINK', 'Pink'
    ORANGE = 'ORANGE', 'Orange'
    BROWN = 'BROWN', 'Brown'

class Card(models.Model):
    identifier = models.CharField(max_length=5)
    type = models.CharField(max_length=255, choices=CardType.choices)
    name = models.CharField(max_length=255)
    description = models.TextField()
    dice = models.ManyToManyField(Die, blank=True)
    # symbols = 
    pawns = models.CharField(max_length=255, choices=Pawn.choices, blank=True)
    weapon_level = models.CharField(max_length=255, blank=True)
    cabbage = models.IntegerField(null=True, blank=True)
    radish = models.IntegerField(null=True, blank=True)
    water = models.IntegerField(null=True, blank=True)
    milk = models.IntegerField(null=True, blank=True)
    psi = models.IntegerField(null=True, blank=True)
    # special_series = 
    # series = 

    def __str__(self):
        return self.name