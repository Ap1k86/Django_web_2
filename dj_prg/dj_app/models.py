from django.db import models


# Модель человек.
class Person(models.Model):
    name = models.CharField(max_length=15)
    age = models.IntegerField()
    objects = models.Model


# Модель компания
class Company(models.Model):
    name = models.CharField(max_length=30)
    objects = models.Model


# Модель продукт
class Product(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    objects = models.Model
