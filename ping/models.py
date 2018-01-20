from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Ping(models.Model):
    user = models.OneToOneField(User, models.CASCADE, primary_key=True)
    pinging = models.BooleanField(default=False)

    def __str__(self):
        return "{}: {}".format(self.user, self.pinging)
