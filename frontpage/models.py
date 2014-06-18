from django.db import models


# Create your models here.
class Data(models.Model):
    key = models.CharField(max_length=20)
    value = models.TextField()

    def __str__(self):
        return self.key
