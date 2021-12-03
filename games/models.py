from django.db import models

# Create your models here.
class Game(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='games/')
    gif = models.ImageField(upload_to='game_gifs/')
    location = models.CharField(max_length=200)
