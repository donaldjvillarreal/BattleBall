
from django.views.generic import ListView, DetailView
from django.contrib.auth import get_user_model
from battleball.forms import UserForm, UserProfileForm
from battleball.models import UserProfile, Game
from django.shortcuts import render
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from .models import Team, Game

import json

def index(request):
		return render(request, 'battleball/newgame_home.html')

#def register(request):

    #registered = False

    #if request.method == 'POST':
        #user_form = UserForm(data=request.POST)
        #profile_form = UserProfileForm(data=request.POST)

        #if user_form.is_valid() and profile_form.is_valid():
            #user = user_form.save()

            #user.set_password(user.password)
            #user.save()

            #profile = profile_form.save(commit=False)
            #profile.user = user

            #if 'picture' in request.FILES:
                    #profile.picture = request.FILES['picture']

            #profile.save()

            #registered = True

        #else:
            #print(user_form.errors, profile_form.errors)

    #else:
        #user_form = UserForm()
        #profile_form = UserProfileForm()

#<<<<<<< working copy
    #return render(request,
            #'battleball/register.html',
           #{'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )


    #return render(request,
            #'battleball/register.html',
            #{'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )

class UserProfileDetailView(DetailView):
    model = get_user_model()
    slug_field = "username"
    template_name = "battleball/user_detail.html"

    def get_object(self, queryset=None):
        user = super(UserProfileDetailView, self).get_object(queryset)
        UserProfile.objects.get_or_create(user=user)
        return user

class UserProfileEditView(UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = "battleball/edit_profile.html"

    def get_object(self, queryset=None):
        return UserProfile.objects.get_or_create(user=self.request.user)[0]

    def get_success_url(self):
        return reverse("profile", kwargs={"slug": self.request.user})
		#>>>>>>> destination

class list_games(ListView):
    '''
    List all playable games in database
    '''
    model = Game
    #return HttpResponse('This will be a list of all games')

def load_game_html(request,game_id):
    '''
    This function will return the base html for the 
    game board
    '''
    game = Game.objects.get(id=game_id)
    context_dict = {'game_id': game_id,
                    'home_team': game.homeTeam,
                    'away_team': game.awayTeam}
    return render(request, 'battleball/game.html', context_dict)

def play_game(request,game_id):
    '''
    This function will return the status of the game 
    board using json
    '''
    game = Game.objects.get(id=game_id)
    with open(str(game.boardFile)) as f:
        game_dict = json.load(f)

    return HttpResponse(json.dumps(game_dict), content_type="application/json")

def board(request):
		'''
		This function will create a game in the database
		and it fills info like team's name and so on.
		It will return gameboard.html
		'''	
		team1 = Team(teamName = 'Red', gamesPlayed = 0, gamesWon = 0, rank = 0)
		team1.save()
		#team2 = Team(teamName = team2_name, gamesPlayed = 0, gamesWon = 0, rank = 0)
		#team2.save()
		return render(request, 'battleball/gameboard.html')

#class GameListView(ListView):
    #model = GameRoom

