import uuid
import random
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Event(models.Model):
    event_name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    begin_date_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    end_date_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    atendee_limit = models.IntegerField(default=0)
    # number_of_tickets = models.IntegerField(default=0)
    event_price = models.IntegerField(default=0)

class Venue(models.Model):
    venue_name = models.CharField(max_length=200)
    seating_capacity = models.IntegerField(default=0)
