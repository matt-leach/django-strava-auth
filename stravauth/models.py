from django.contrib.auth.models import User
from django.db import models



class StravaToken(models.Model):
    user = models.OneToOneField(User)
    token = models.CharField(max_length=60)
    