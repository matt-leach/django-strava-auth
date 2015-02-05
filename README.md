django-strava-auth
==================

[![Build Status](https://travis-ci.org/matt-leach/django-strava-auth.svg?branch=master)](https://travis-ci.org/matt-leach/django-strava-auth)

Module designed to add authentication using the Strava V3 API.

Usage
-----

1. Add 'stravauth' to settings.INSTALLED_APPS
2. Set settings.AUTHENTICATION_BACKENDS = ('stravauth.backend.StravaV3Backend', )
3. Add CLIENT_ID, CLIENT_SECRET, STRAVA_REDIRECT to settings
4. Add to urls: url(r'^login/', StravaAuth.as_view(url=reverse_lazy("home")), kwargs={"approval_prompt": "force"})
