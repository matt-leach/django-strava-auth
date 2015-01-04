from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.core.urlresolvers import reverse_lazy

from stravauth.views import StravaAuth

from app.views import HomeView

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^login/', StravaAuth.as_view(url=reverse_lazy("home")), kwargs={"approval_prompt": "force"}, name="login"),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name="logout"),
)
