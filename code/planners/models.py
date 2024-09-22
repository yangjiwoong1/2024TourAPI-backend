from django.db import models
from django.conf import settings

class Plan(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, to_field='username', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Destination(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    content_id = models.IntegerField()
    content_title = models.CharField(max_length=150)
    custom_name = models.CharField(max_length=150, blank=True, null=True)
    gpsX = models.DecimalField(max_digits=10, decimal_places=7)
    gpsY = models.DecimalField(max_digits=10, decimal_places=7)
    visit_date = models.DateField()
    visit_time = models.TimeField()

    class Meta:
        unique_together = ('plan', 'content_id')

    def __str__(self):
        return self.content_title
