from django.conf import settings
from django.contrib.auth import login, authenticate as strava_authenticate
from django import http
from django.shortcuts import redirect
from django.views.generic import RedirectView


class StravaRedirect(RedirectView):
    """
        Redirects to the Strava oauth page
    """
    def get_redirect_url(self, approval_prompt="force", scope="write", *args, **kwargs):
        from django.conf import settings
        
        strava_url = "https://app.strava.com/oauth/authorize"
        vars = ""
        vars += "client_id=%s" % settings.CLIENT_ID
        vars += "&response_type=%s" % "code"
        vars += "&redirect_uri=%s" % settings.STRAVA_REDIRECT
        vars += "&approval_prompt=%s" % approval_prompt
        vars += "&scope=%s" % scope
                
        return "%s?%s" % (strava_url, vars)


class StravaAuth(RedirectView):
    
    def get(self, request, *args, **kwargs):
        code = request.GET.get("code", None)
        
        print "strava auth redirect view"
        
        if code:
            # Log the user in
            user = strava_authenticate(code=code)
            login(request, user)
            url = self.get_redirect_url(code=code, *args, **kwargs)
        else:
            # Redirect to the strava url
            view = StravaRedirect.as_view()
            return view(request, *args, **kwargs)
        
        if url:
            if self.permanent:
                return http.HttpResponsePermanentRedirect(url)
            else:
                return http.HttpResponseRedirect(url)
        else:
            logger.warning('Gone: %s', request.path,
                        extra={
                            'status_code': 410,
                            'request': request
                        })
            return http.HttpResponseGone()
    
    
    
    
    