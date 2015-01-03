from django.http import HttpResponse


def home(request):
    return HttpResponse("Home. User: %s" % request.user.username)