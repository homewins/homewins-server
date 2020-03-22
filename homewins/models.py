from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Profile(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    score = models.PositiveIntegerField()

    class Meta:
        ordering = ['created']

    def __str__(self):
        return "Profile({})".format(self.owner.username)
