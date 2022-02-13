from django.db import models

# Create your models here.
class Card(models.Model):
    
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    price = models.IntegerField(default=0)
    verified_card = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Print(models.Model):

    name = models.CharField(max_length=100, default= str)
    img = models.CharField(max_length=250)
    price = models.IntegerField(default=0)
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name="cards")

    def __str__(self):
        return self.name