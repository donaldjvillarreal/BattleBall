
from django.views.generic import ListView, DetailView
from django.contrib.auth import get_user_model
from battleball.forms import UserForm, UserProfileForm
from battleball.models import UserProfile, GameRoom, Game
from django.shortcuts import render
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse

def index(request):
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render(request, 'battleball/index.html', context_dict)

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
    return render(request,
            'battleball/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )


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

def board(request):
    return render(request, 'battleball/gameboard.html')
#>>>>>>> destination

def index(request):
    return HttpResponse("Hello, world. You're at the battleball index.")

def list_games(request):
    '''
    List all playable games in database
    '''
    return HttpResponse('This will be a list of all games')

def load_game_html(request,game_id):
    '''
    This function will return the base html for the 
    game board
    '''
    return render(request, 'battleball/game.html')

def play_game(request,game_id):
    '''
    This function will return the status of the game 
    board using json
    '''
    return HttpResponse('This will be the json for game: %s' % game_id)

class GameListView(ListView):
    model = GameRoom

