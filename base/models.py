from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator

# Create your models here.

#genre table 

class Genre(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
#Universes table
class Universe(models.Model):
    name = models.CharField(max_length=200)
    total_movies = models.PositiveIntegerField()
    description = models.TextField(null = True)
    genres = models.ManyToManyField('Genre',related_name='type')
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(5)],null=True)
    image = models.ImageField(upload_to='universe/img',null=True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    
    def __str__(self):
        return self.name
    
#Movie Table    
class Movie(models.Model):
    title = models.CharField(max_length=200)
    director = models.CharField(max_length=200)
    release_date = models.DateField()
    watching_link = models.URLField()
    image = models.ImageField(upload_to='Djangoweb/cin')
    gross_income = models.PositiveIntegerField(null=True)
    universe = models.ForeignKey(Universe, on_delete=models.CASCADE, related_name='movies')

#Messages table
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Universe, on_delete=models.CASCADE)
    body = models.TextField()
    
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-updated','-created']
    
    
    def __str__(self):
        return self.body[0:50]


from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)    
    fullname = models.CharField(max_length=100, blank=True, null=True)
    interested_genres = models.CharField(max_length=100, blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    interest_topics = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username + ' Profile'

