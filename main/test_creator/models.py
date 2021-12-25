from django.db import models
import uuid


class Test(models.Model):
    id = uuid.uuid4()


class Choises(models.Model):
    text = models.CharField(max_length=512)
    photo = models.TextField()
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
