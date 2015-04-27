'''
Databases for battleball
'''

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# This block of code is added by Donald

class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True)

    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username

def create_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = UserProfile.objects.get_or_create(user=instance)

post_save.connect(create_profile, sender=User)

class Game(models.Model):
    ''' crucial items for game board '''
    title = models.CharField("Title", max_length=100, default='untitled')
    url = models.URLField("URL", max_length=250, blank=True)
    boardFile = models.CharField(max_length=30, default=0)
    homeTeam = models.CharField(max_length=30)
    awayTeam = models.CharField(max_length=30)
    turn = models.BooleanField(default=True)
    homeScore = models.IntegerField(default=0)
    awayScore = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

# These blocks of code is added by Tenzin
class Team(models.Model):
    ''' Team name and stats '''
    teamName = models.CharField(max_length=30)
    gamesPlayed = models.IntegerField(default=0)
    gamesWon = models.IntegerField(default=0)
    rank = models.IntegerField(default=0)
    def __str__(self):
        return self.teamName
+<<<<<<< destination:f23f2a17fe34eb7a18062f619150694c91b97ea9:app/battleball/models.py

class User(models.Model):
    ''' Individual user '''
    team = models.ForeignKey(Team)
    fullName = models.CharField(max_length=30)
    userName = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    dateJoined = models.DateTimeField('Date Joined')
    def __str__(self):
        return self.userName


+=======
+>>>>>>> source:2874c772243ffeb972811792619e91db5e6ac9b7:app/battleball/models.py
