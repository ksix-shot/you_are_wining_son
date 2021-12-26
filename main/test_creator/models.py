from django.db import models
import uuid
from django.utils import timezone


class Test(models.Model):
    id = uuid.uuid4()
    name = models.CharField(max_length=512, default=str(id))
    date_creation = models.DateTimeField(default=timezone.now)
    date_last_change = models.DateTimeField(default=timezone.now)


class Choises(models.Model):
    text = models.CharField(max_length=512)
    photo = models.TextField(blank=True, null=True)
    youtube_url = models.CharField(max_length=512, default=None, blank=True, null=True)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
