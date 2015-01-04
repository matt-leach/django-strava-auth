import requests


class StravaClient(object):
    """
    Object used to access Strava API
    """
    api_endpoint = "https://www.strava.com"
    
    def get_token(self, client_id, client_secret, code):
        data = {"client_id": client_id, "client_secret": client_secret, "code": code}
        
        r = requests.post("%s/oauth/token" % self.api_endpoint, data=data)
                
        # TODO: Error handling 
        response = r.json()
        
        return response
