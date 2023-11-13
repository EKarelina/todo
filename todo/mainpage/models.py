
from django.db import models
from datetime import datetime

# В этом файле принято создавать классы, описывающие
# структуры необходимых приложению таблиц


# https://docs.djangoproject.com/en/4.2/topics/db/models/
class Task(models.Model):
    # id создастся сам!
    start = models.DateTimeField(default=datetime.now)
    end = models.DateTimeField()
    description = models.CharField(max_length=256, default='')
    done = models.BooleanField(default=False)


class Kategorii(models.Model):
    kategoriya = models.CharField(max_length=20, unique=True)


class Goods(models.Model):
    picture = models.ImageField()
    namegoods = models.CharField(max_length=20)
    price = models.FloatField()
    quantity = models.FloatField()
    pricetotal = models.FloatField()
