from django import template

from stravauth.utils import get_stravauth_url

register = template.Library()

@register.tag(name='stravauth_url')
def stravauth_url_tag(parser, format):
    return StravauthUrlNode()
    
    
class StravauthUrlNode(template.Node):
    def __init__(self):
        pass
    
    def render(self, context):
        
        return get_stravauth_url()