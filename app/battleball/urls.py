from django.conf.urls import patterns, url
from battleball import views

urlpatterns = patterns('',
  url(r'^$', views.index, name='index'))
