from django.db import models


# Класс человек.
class Person(models.Model):
    name = models.CharField(max_length=15)
    age = models.IntegerField()
    objects = models.Model
