'''
This file contains all the set ups for forms
'''
from django import forms
from django.contrib.auth.models import User
from battleball.models import UserProfile, Game

class UserForm(forms.ModelForm):
    ''' Registration Form '''
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta(object):
        ''' additional fields '''
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    ''' Profile Page '''
    class Meta(object):
        ''' additional fields '''
        model = UserProfile
        exclude = ("user",)

class GameForm(forms.ModelForm):
    '''
    Create Game Form
    '''
    class Meta(object):
        model = Game
        exclude = ("url","boardFile","turn","homeScore","awayScore",)