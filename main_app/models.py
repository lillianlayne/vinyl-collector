from django.db import models
from django.urls import reverse

# Create your models here.
class Vinyl(models.Model):
    name = models.CharField(max_length=300)
    artist = models.CharField(max_length=300)
    release_year = models.IntegerField()
    song_count = models.IntegerField()
    genre = models.CharField(max_length=300)

    def __str__(self): 
        return f'self.name ({self.id})'

    def get_absolute_url(self):
        return reverse("detail", kwargs={"viny_id": self.id})
    