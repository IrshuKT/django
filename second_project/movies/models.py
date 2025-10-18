from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    rating = models.FloatField()
    thumbnail = models.ImageField(upload_to='movies/thumbnails/', blank=True, null=True)
    censor_info = models.OneToOneField('CensorInfo', on_delete=models.CASCADE, null=True,related_name='movie')
    directed_by = models.ForeignKey('Director', on_delete=models.CASCADE, null=True,related_name='directed_movies')
    actors = models.ManyToManyField('Actor', related_name='movies', blank=True)

    def __str__(self):
        return self.name
    

class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class CensorInfo(models.Model):
    rating = models.CharField(max_length=10)
    certified_by = models.fields.CharField(max_length=300)

    def __str__(self):
        return self.rating

class Actor(models.Model):
    name = models.CharField(max_length=100)
    #movies = models.ManyToManyField(Movie, related_name='actors')

    def __str__(self):
        return self.name


