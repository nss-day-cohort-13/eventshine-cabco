import uuid
import random
from django.db import models
from django.contrib.auth.models import User



class Venue(models.Model):
    """
    This class will hold the Venue.
    This will hold the:
        Venue Name and Seating Capacity.

    Character Field limit is 200.

    """
    venue_name = models.CharField(max_length=200)
    seating_capacity = models.IntegerField(default=0)


class Event(models.Model):
    """
    This class will hold the Event.
    This will hold the:
        Event Name, Description, City, Begin Date, End Date
        Attendee Limit, Number of Tickets, and Event price.

    Character Field limit is 200.
    """
    event_name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    begin_date_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    end_date_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    atendee_limit = models.IntegerField(default=0)
    # number_of_tickets = models.IntegerField(default=0)
    event_price = models.IntegerField(default=0)
    event_creator = models.ForeignKey(User, on_delete=models.CASCADE)
    event_venue = models.ForeignKey(Venue)



# class Ticket(models.Model):