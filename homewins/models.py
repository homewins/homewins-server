from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Profile(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    score = models.PositiveIntegerField()
    ssid = models.CharField(max_length=100)
    latlong = models.CharField(max_length=100)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return "Profile({})".format(self.owner.username)
