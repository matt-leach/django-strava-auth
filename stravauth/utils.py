

def get_stravauth_url(approval_prompt="auto", scope="write"):
    """
        Function that returns the strava oauth url for your 
        project
    """
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