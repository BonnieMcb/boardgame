from django.db import models
from django.contrib.auth.models import User

class Membership(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    expiry = models.DateField()
    is_premium = models.BooleanField()

    def __str__(self):
        return "foo"
