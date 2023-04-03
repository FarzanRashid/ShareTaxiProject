from django.db import models


class RideRequest(models.Model):
    destination_location = models.CharField(max_length=200)
    departure_time = models.TimeField()
    email = models.EmailField()
    pickup_location = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'RideRequest'
