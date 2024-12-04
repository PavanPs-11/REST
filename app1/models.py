from django.db import models


# Create your models here.
class Example(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    objects = models.Manager()

    def __str__(self):
        return f"{self.name}, Age: {self.age}"