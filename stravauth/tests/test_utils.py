from django.test import TestCase
from django.conf import settings
from stravauth.utils import get_stravauth_url


class TestStravauthUtils(TestCase):
    
    def decompose_url(self, full_url):
        url = full_url.split("?")[0]
        vars_str = full_url.split("?")[1]
        vars = {var.split("=")[0]: var.split("=")[1] for var in vars_str.split("&")}
        return url, vars
    
    def test_get_stravauth_url_no_params(self):
        url = get_stravauth_url()
        url, vars = self.decompose_url(url)
        self.assertEqual(url, "https://app.strava.com/oauth/authorize")
        
        self.assertEqual(len(vars), 5)
        self.assertEqual(vars["client_id"], str(settings.CLIENT_ID))
        self.assertEqual(vars["response_type"], "code")
        self.assertEqual(vars["redirect_uri"], settings.STRAVA_REDIRECT)
        self.assertEqual(vars["approval_prompt"], "auto")
        self.assertEqual(vars["scope"], "write")

        
        
        
        