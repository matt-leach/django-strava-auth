from mock import patch

from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.contrib.auth import authenticate            

from stravauth.client import StravaClient
from stravauth.models import StravaToken


class TestStravaAuthenticationWithMockedAPI(TestCase):
    """
        Tests for the backend StravaV3Backend using
        a mock object for the Strava API
    """
    def fake_get_token(self, client_id, client_secret, code):
        """
        Mock get_token method
        """
        if code == "alice code": 
            return {"access_token": "alice token", "athlete": {"id": 1, "first_name": "alice"}}
        else: 
            raise Exception()
        
    @patch.object(StravaClient, 'get_token', fake_get_token)
    def test_authorize_user_does_not_exist(self):
        user_created = authenticate(code="alice code")
                   
        # Test now one user
        self.assertEqual(len(User.objects.all()), 1)      
        u = User.objects.all()[0]
           
        # Check it's the same 
        self.assertEqual(user_created, u)
        
        # Check the user has the properties we expect 
        self.assertEqual(u.username, "alice ")
        self.assertEqual(u.password, "")
        self.assertEqual(u.is_superuser, False)
        
        # Check the user has a token
        self.assertEqual(u.stravatoken.token, "alice token")

    @patch.object(StravaClient, 'get_token', fake_get_token)
    def test_authorize_user_does_exist(self):          
        # Create the user we'll reference    
        self.assertEqual(len(User.objects.all()), 0)
        u = User.objects.create(id=1, username="user 1")
                     
        user_got = authenticate(code="alice code")
             
        # Check the user has the token
        self.assertEqual(user_got.stravatoken.token, "alice token")
             
        # Test still one user, and it's the same
        self.assertEqual(len(User.objects.all()), 1)
        self.assertEqual(user_got, u)
        
    @patch.object(StravaClient, 'get_token', fake_get_token)
    def test_authorize_user_already_has_token(self):
        # Create the user we'll reference    
        self.assertEqual(len(User.objects.all()), 0)
        u = User.objects.create(id=1, username="user 1")
        
        # Create the token
        token = StravaToken.objects.create(token="token before", user=u)
        u = User.objects.create(id=1, username="user 1") 
    
        user_got = authenticate(code="alice code")
             
        # Check the user has the uupdated token
        self.assertEqual(user_got.stravatoken.token, "alice token")

    
    @patch.object(StravaClient, 'get_token', fake_get_token)    
    def test_authorize_when_get_token_failed(self):
        user = authenticate(code="eve token")
        
        # Failed auth should return no user
        self.assertTrue(user is None)
        
            