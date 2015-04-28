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

class Piece(models.Model):
    ''' piece on the team '''
    def __init__(self, *args, **kwargs):
        return super(Piece, self).__init__(*args, **kwargs)
    name = models.CharField(max_length=30)
    piece_size = models.IntegerField(default=1)
    has_ball = models.BooleanField(default=False)
    injury = models.IntegerField(default='0')
    str_position = models.CharField(max_length=20, default='{"xpos":-1, "ypos":-1}')
    roll_size = models.IntegerField(default=20)

    def __unicode__(self):
        return self.name

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

    def instatiate_pieces():
        heavy_tackle_h = Piece(roll_size=6, piece_size=2, name='heavy tackle')
        tackle_h = Piece(roll_size=6, piece_size=1, name='tackle')
        lineman1_h = Piece(roll_size=8, piece_size=1, name='lineman 1')
        lineman2_h = Piece(roll_size=8, piece_size=1, name='lineman 2')
        linebacker1_h = Piece(roll_size=10, piece_size=1, name='linebacker 1')
        linebacker2_h = Piece(roll_size=10, piece_size=1, name='linebacker 2')
        safety1_h = Piece(roll_size=12, piece_size=1, name='safety 1')
        safety2_h = Piece(roll_size=12, piece_size=1, name='safety 2')
        running_back1_h = Piece(roll_size=20, piece_size=1, name='running back 1')
        running_back2_h = Piece(roll_size=20, piece_size=1, name='running back 2')
        running_back3_h = Piece(roll_size=20, piece_size=1, name='running back 3')

        heavy_tackle_a = Piece(roll_size=6, piece_size=2, name='heavy tackle')
        tackle_a = Piece(roll_size=6, piece_size=1, name='tackle')
        lineman1_a = Piece(roll_size=8, piece_size=1, name='lineman 1')
        lineman2_a = Piece(roll_size=8, piece_size=1, name='lineman 2')
        linebacker1_a = Piece(roll_size=10, piece_size=1, name='linebacker 1')
        linebacker2_a = Piece(roll_size=10, piece_size=1, name='linebacker 2')
        safety1_a = Piece(roll_size=12, piece_size=1, name='safety 1')
        safety2_a = Piece(roll_size=12, piece_size=1, name='safety 2')
        running_back1_a = Piece(roll_size=20, piece_size=1, name='running back 1')
        running_back2_a = Piece(roll_size=20, piece_size=1, name='running back 2')
        running_back3_a = Piece(roll_size=20, piece_size=1, name='running back 3')

        player_dict = {'home': [heavy_tackle_h, tackle_h, lineman1_h, lineman2_h,
                                linebacker1_h, linebacker2_h, safety1_h, safety2_h,
                                running_back1_h, running_back2_h, running_back3_h],

                    'away': [heavy_tackle_a, tackle_a, lineman1_a, lineman2_a,
                                linebacker1_a, linebacker2_a, safety1_a, safety2_a,
                                running_back1_a, running_back2_a, running_back3_a]}

        return player_dict

    pieces = instatiate_pieces()

    def __unicode__(self):
        return self.title

class Coach(models.Model):
    ''' users can create a coach '''
    name = models.CharField(max_length=30)
    user = models.OneToOneField(User, unique=True)

    def __unicode__(self):
        return self.name


# These blocks of code is added by Tenzin
class Team(models.Model):
    ''' Team name and stats '''
    teamName = models.CharField(max_length=30)
    gamesPlayed = models.IntegerField(default=0)
    gamesWon = models.IntegerField(default=0)
    rank = models.IntegerField(default=0)
    def __str__(self):
        return self.teamName

