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
        try:
            response = c.get_token(client_id, client_secret, code)
        except: # TODO: specific exception
            return None
                
        access_token = response["access_token"]
        user_id = response["athlete"]["id"]
        
        # username must be unique hence use id
        username = "%s: %s %s" % (user_id, response["athlete"]["firstname"], response["athlete"]["lastname"])
        
        # Get or create the user (returns tuple)
        try:
            user = User.objects.get(id=user_id)
        except:
            user = User(id=user_id)
        
        # Update username
        user.username = username
        user.save()  
        
        # Add the token 
        (token_model, created) = StravaToken.objects.get_or_create(user=user)            
        token_model.token = access_token
        token_model.save()
        
        # Return the user
        return user
        
    
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None