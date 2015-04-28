'''
This file contains everything for the admins
'''
from django.contrib import admin
from battleball.models import UserProfile
from battleball.models import Game, Coach, Piece
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

#admin.site.register(UserProfile)

admin.site.register(Game)
admin.site.register(Coach)
admin.site.register(Piece)

class UserProfileInline(admin.StackedInline):
    ''' Inline for User Profile '''
    model = UserProfile
    can_delete = False

class UserProfileAdmin(UserAdmin):
    ''' Admin's view to User Profile '''
    inlines = (UserProfileInline, )

admin.site.unregister(get_user_model())
admin.site.register(get_user_model(), UserProfileAdmin)
