from django.conf import settings
from django.contrib.auth.models import User

from stravauth.client import StravaClient
from stravauth.models import StravaToken 

class StravaV3Backend(object):
    """
    Authenticate using the Strava V3 API.
    """
    def authenticate(self, code):
        client_id = settings.CLIENT_ID
        client_secret = settings.CLIENT_SECRET
        
        # Make the request to the API
        c = StravaClient()
        response = c.get_token(client_id, client_secret, code)
        
        access_token = response["access_token"]
        user_id = response["athlete"]["id"]
        username = "%s %s" % (response["athlete"]["firstname"], response["athlete"]["lastname"])
        
        # Get or create the user
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            # Otherwise create the user
            user = User(id=user_id, username=username)
            user.save()  
        
        # Add the token 
        try:
            token_model = user.stravatoken
        except StravaToken.DoesNotExist:
            token_model = StravaToken(user=user)
            
        token_model.token = access_token
        token_model.save()
        
        # Return the user
        return user
        
        