from django.db import models
from django.utils import timezone
import datetime
from django.contrib import admin

# Create your models here.

class WYR_Users(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=40)

    date_joined = models.DateField("Date user joined")

class Category(models.Model):
    #Stores all the categories going to the Scenario
    category = models.CharField(max_length=70)
    


class Scenario(models.Model):
    scenario_question = models.CharField(max_length=750)
    votes = models.IntegerField(default=0)
    category_choice =  models.ManyToManyField(Category)


    date_published = models.DateTimeField("Date scenario was published")

    created_by = models.ForeignKey(WYR_Users.username, on_delete=models.SET_NULL ,null=True)

    def __str__(self):
        return self.scenario_question
