from django.db import models
from django.conf import settings

class Place(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL, to_field='username', on_delete=models.CASCADE)
    content_id = models.IntegerField()
    content_title = models.CharField(max_length=150)
    gpsX = models.DecimalField(max_digits=10, decimal_places=7)
    gpsY = models.DecimalField(max_digits=10, decimal_places=7)

    def __str__(self):
        return self.content_title