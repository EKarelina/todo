
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
