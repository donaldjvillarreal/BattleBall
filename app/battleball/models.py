from django.db import models
from django.contrib.auth.models import User

# This block of code is added by Donald
class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True)

    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username

def create_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = UserProfile.objects.get_or_create(user=instance)

from django.db.models.signals import post_save
post_save.connect(create_profile, sender=User)

# These blocks of code is added by Tenzin
class Team(models.Model):
	teamName = models.CharField(max_length = 30)
	gamesPlayed = models.IntegerField(default=0)
	gamesWon = models.IntegerField(default=0)
	rank = models.IntegerField()
	def __str__(self):
		return self.teamName

class User(models.Model):
	team = models.ForeignKey(Team)
	fullName = models.CharField(max_length = 30)
	userName = models.CharField(max_length = 30)
	password = models.CharField(max_length = 30)
	dateJoined = models.DateTimeField('Date Joined')
	def __str__(self):
		return self.userName

class Game(models.Model):
	boardState = models.CharField(max_length = 30, default = 0)
	homeTeam = models.CharField(max_length = 30)
	awayTeam = models.CharField(max_length = 30)
	homeScore = models.IntegerField(default=0)
	awayScore = models.IntegerField(default=0)
	def __str__(self):
		return self.boardState

