from django.conf import settings
from django.contrib.auth import login, authenticate as strava_authenticate
from django import http
from django.shortcuts import redirect
from django.views import generic


class StravaRedirect(generic.RedirectView):
    """
        Redirects to the Strava oauth page
    """
    def get_redirect_url(self, approval_prompt="auto", scope="write", *args, **kwargs):
        from django.conf import settings
        
        # TODO: check scope and approval_prompt are reasonable 
        
        strava_url = "https://app.strava.com/oauth/authorize"
        vars = ""
        vars += "client_id=%s" % settings.CLIENT_ID
        vars += "&response_type=%s" % "code"
        vars += "&redirect_uri=%s" % settings.STRAVA_REDIRECT
        vars += "&approval_prompt=%s" % approval_prompt
        vars += "&scope=%s" % scope
                
        return "%s?%s" % (strava_url, vars)


class StravaAuth(generic.View):
    url = None # Or default?
    
    def get(self, request, *args, **kwargs):        
        code = request.GET.get("code", None)
                
        if not code:
            # Redirect to the strava url
            view = StravaRedirect.as_view()
            return view(request, *args, **kwargs)
        
        # Log the user in
        user = strava_authenticate(code=code)
        login(request, user)
                    
        return http.HttpResponseRedirect(self.url)
        
    
    
    
    