from django.conf.urls import patterns, url, include
from django.contrib.auth.decorators import login_required as auth
from battleball import views
from django.contrib import admin
admin.autodiscover()
from battleball.views import UserProfileDetailView
from battleball.views import UserProfileEditView
#from battleball.views import UserProfileDetailView
#from battleball.views import UserProfileEditView

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    #url(r'^register/$', views.register, name='register'),
		url(r'^board/$', views.board, name='board'), 

    url(r'^account/', include('registration.backends.simple.urls')),
    url(r"^login/$", "django.contrib.auth.views.login",
        {"template_name": "battleball/login.html"}, name="login"),
    url(r"^logout/$", "django.contrib.auth.views.logout_then_login",
        name="logout"),
    url(r"^users/(?P<slug>\w+)/$", UserProfileDetailView.as_view(),
        name="profile"),
    url(r"edit_profile/$", auth(UserProfileEditView.as_view()),
        name="edit_profile"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^board/$', views.list_games.as_view(), name='games'),
    url(r'^board/(?P<game_id>[0-9]+)/$', views.load_game_html, name='load_game_html'),
    url(r'^board/(?P<game_id>[0-9]+)/game/$', views.play_game, name='play_game'),
    url(r'^board/(?P<game_id>[0-9]+)/move/$', views.place_piece, name='place_piece'),
    #url(r'^gamelist/', views.list_games.as_view(), name='gamelist'),
    )
