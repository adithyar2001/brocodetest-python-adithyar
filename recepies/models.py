from django.db import models
from django.contrib.postgres.fields import ArrayField

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.CharField(max_length=500)
    categories = models.ManyToManyField(Category)
    def __str__(self):
        return self.name
