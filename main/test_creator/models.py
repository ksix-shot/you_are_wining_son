from django.db import models
import uuid


class Test(models.Model):
    id = uuid.uuid4()
    name = models.CharField(max_length=512, default=str(id))


class Choises(models.Model):
    text = models.CharField(max_length=512)
    photo = models.TextField()
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
