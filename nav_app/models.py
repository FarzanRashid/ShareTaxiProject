from django.db import models


class GetUserInfo(models.Model):
    location = models.CharField(max_length=200)
    departure_time = models.TimeField()
    email = models.EmailField(null=True)
