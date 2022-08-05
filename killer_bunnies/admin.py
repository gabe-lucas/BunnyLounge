from django.contrib import admin

from .models.bunnybit import *
from .models.card import *
from .models.deck import *
from .models.die import *
from .models.game import *

# Register your models here.

admin.site.register(Bunnybit)
admin.site.register(Card)
admin.site.register(Deck)
admin.site.register(Die)
admin.site.register(Game)