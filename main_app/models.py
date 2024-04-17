from django.db import models
from django.urls import reverse



# Create your models here.
class Genre(models.Model):
    name = models.CharField(
        max_length=200    )

    def __str__(self):
        return f'{self.name} ({self.id})'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'genre_id': self.id})


class Vinyl(models.Model):
    name = models.CharField(max_length=300)
    artist = models.CharField(max_length=300)
    release_year = models.IntegerField()
    genres = models.ManyToManyField(Genre)

    def __str__(self): 
        return f'{self.name }({self.id})'

    def get_absolute_url(self):
        return reverse("detail", kwargs={"vinyl_id": self.id})


class Songs(models.Model): 
    title = models.CharField(max_length=200)
    song_length = models.IntegerField()

    vinyl = models.ForeignKey(Vinyl, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'


class Photo(models.Model):
    url = models.CharField(max_length=500)
    vinyl = models.ForeignKey(Vinyl, on_delete=models.CASCADE)

    def __str__(self):
        return f'photo for vinyl_id: {self.vinyl_id} @ {self.url}'