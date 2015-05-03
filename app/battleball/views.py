''' views for the battleball app '''
from django.views.generic import ListView, DetailView
from django.contrib.auth import get_user_model
from battleball.forms import UserForm, UserProfileForm
from battleball.models import UserProfile, Game, Piece
from django.shortcuts import render
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse
from django.http import HttpResponse

import json

def index(request):
    ''' returns startgame.html '''
    return render(request, 'battleball/index.html')

class UserProfileDetailView(DetailView):
    ''' views for user profile '''
    model = get_user_model()
    slug_field = "username"
    template_name = "battleball/user_detail.html"

    def get_object(self, queryset=None):
        user = super(UserProfileDetailView, self).get_object(queryset)
        UserProfile.objects.get_or_create(user=user)
        return user

class UserProfileEditView(UpdateView):
    ''' view for editing user profile '''
    model = UserProfile
    form_class = UserProfileForm
    template_name = "battleball/edit_profile.html"

    def get_object(self, queryset=None):
        return UserProfile.objects.get_or_create(user=self.request.user)[0]

    def get_success_url(self):
        return reverse("profile", kwargs={"slug": self.request.user})

#def board(request):
#    ''' views for gameboard '''
#    return render(request, 'battleball/gameboard.html')

class list_games(ListView):
    '''
    List all playable games in database
    '''
    model = Game
    #return HttpResponse('This will be a list of all games')

def load_game_html(request, game_id):
    '''
    This function will return the base html for the
    game board
    '''
    game = Game.objects.get(id=game_id)
    context_dict = {'game_id': game_id,
                    'home_team': game.homeTeam,
                    'away_team': game.awayTeam}
    return render(request, 'battleball/game.html', context_dict)

def play_game(request, game_id):
    '''
    This function will return the status of the game
    board using json
    '''
    game = Game.objects.get(id=game_id)
    with open(str(game.boardFile)) as f:
        game_dict = json.load(f)



    return HttpResponse(json.dumps(game_dict), content_type="application/json")

def update_game_model(request, game_id):
    '''
    This function will update the game model with
    the board from the put request
    '''
    new_board = request.content
    game = Game.objects.get(id=game_id)
    with open(str(game.boardFile), 'r+') as f:
        game_dict = json.load(f)
        game_dict[pos["xpos"]][pos["ypos"]] = piece.name
        f.seek(0)
        f.write(json.dumps(new_board))
        f.truncate()

    return HttpResponse(json.dumps(game_dict), content_type="application/json")
