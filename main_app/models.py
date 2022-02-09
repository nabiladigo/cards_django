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

# class Song(models.Model):
    
#     title = models.CharField(max_length=150)
#     length = models.IntegerField(default=0)
#     artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="songs")

#     def __str__(self):
#         return self.title