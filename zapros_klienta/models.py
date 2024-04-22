from django.db import models


class Landmark(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    photo = models.ImageField(upload_to='landmark_photos/')
    work_schedule = models.CharField(max_length=255, blank=True, null=True)
    price = models.CharField(max_length=100, blank=True, null=True)
    contacts = models.CharField(max_length=255, blank=True, null=True)
    history_fact = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
