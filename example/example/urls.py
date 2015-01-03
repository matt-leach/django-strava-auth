from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.core.urlresolvers import reverse_lazy

from stravauth.views import StravaAuth

urlpatterns = patterns('',
    url(r'^$', 'example.views.home', name="home"),
    url(r'^login/', StravaAuth.as_view(url=reverse_lazy("home")), kwargs={"approval_prompt": "force"}),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
)
