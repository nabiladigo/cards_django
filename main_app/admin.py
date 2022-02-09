from django.contrib import admin
from .models import Card,  Print# import the Artist model from models.py
# Register your models here.

admin.site.register(Card) # this line will add the model to the admin panel
admin.site.register(Print) # this line will add the model to the admin panel