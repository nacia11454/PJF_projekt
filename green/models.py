import datetime

from django.db import models
from django.utils import timezone

class Group(models.Model):
    name_gr = models.CharField(max_length=100)
    sun = models.IntegerField(default = 5)
    water = models.IntegerField(default = 5)
    def __str__(self):
        return self.name_gr

class Plant(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    name_pl = models.CharField(max_length=100)
    likes = models.IntegerField(default = 0)
    def __str__(self):
        return self.name_pl
        
class User(models.Model):
    name_us = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    def __str__(self):
        return self.name_us
     
class Care(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    care_date = models.DateTimeField('Data pielegnacji')
    note = models.CharField(max_length=200)
    def __str__(self):
        return self.id
    def was_care_recently(self):
        return self.care_date >= timezone.now() - datetime.timedelta(days=1)   