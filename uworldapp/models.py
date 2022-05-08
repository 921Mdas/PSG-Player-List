from turtle import position
from django.db import models
from django.contrib.auth.models import User
from django.forms import model_to_dict

# Create your models here.

class Trophees(models.Model):
    trophee = models.CharField(max_length=100, default="no trophee")
    year = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return f'{self.trophee} won in {self.year}'

class Performance(models.Model):
    speed = models.IntegerField(default=60)
    stamina = models.IntegerField(default=90)
    passing = models.IntegerField(default=7)
    
    def __str__(self):
        return f'speed:{self.speed}, stamina:{self.stamina}, passing:{self.passing}'
    class Meta:
            verbose_name_plural = 'Performance'

class Player(models.Model):
    FR = 'French'
    EN = 'English'
    SP = 'Spanish'
    PT = 'Portuguese'
    MD = 'Middlefield'
    ST = 'Striker'
    GK = 'Goalkeeper'
    RS = 'Reserve'
    DFL = "Select a language"
    DFP = "Select a position"
    languages = (
        (DFL,"Select a language"),
        (FR,'French'),
        (EN,'English'),
        (SP,'Spanish'),
        (PT,'Portuguese')
    )

    positions = (
        (DFP,"Select a position"),
        (MD,'Middlefield'),
        (ST,'Striker'),
        (GK,'Goalkeeper'),
        (RS,'Reserve')
    )
    name = models.CharField(max_length=100, default="John Doe")
    language = models.CharField(max_length=50,choices=languages,default=DFL)
    position = models.CharField(max_length=50,choices=positions,default=DFP)
    score = models.ForeignKey(Performance, on_delete=models.CASCADE, blank=True)
    trophy =  models.ManyToManyField(Trophees)
    user = models.ForeignKey(User, on_delete=models.CASCADE , default=1)

    def __str__(self):
            return self.name
    class Meta:
            verbose_name_plural = 'Player'


class Photo(models.Model):
    url = models.CharField(max_length=200)
    player = models.ForeignKey(Player,  on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for player id: {self.player_id} @{self.url}"

class Club(models.Model):
    name = models.CharField(max_length=300, blank=True)
    nationality = models.CharField(max_length=200, blank=True)
