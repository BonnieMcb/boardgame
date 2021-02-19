from django.db import models

from profiles.models import UserProfile


class Events(models.Model):
    """
    A model to add events as admin, and
    display events on the event page.
    """
    name = models.CharField(max_length=254)
    datetime = models.DateTimeField()
    description = models.TextField()
    image = models.ImageField(blank=True, upload_to='uploads/')
    offsite_url = models.URLField(blank=True)
    member_only = models.BooleanField()
    signed_up_users = models.ManyToManyField(
        UserProfile, blank=True,)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        print("save the daaaaate")

