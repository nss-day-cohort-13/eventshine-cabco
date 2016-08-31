from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.generic import TemplateView
from .models import Event, Venue
from django.template import RequestContext
import json
from django.core import serializers
from django.contrib.auth import logout

from django.contrib.auth.models import User

from django.contrib.auth import authenticate

# Create your views here.
def index(request):
    """
    This class is for our Index.
    """
    template_name = 'index.html'
    return render(request, template_name, {})


# VIEWS CATCH 'POST'  <-----LOOK AT THAT, WOW.


# CREATE USER #
# @csrf_exempt
def create_user_object(request):
    '''
        Function to catch registration of user from login.html.
        Upon form submission, the values of the fields are passed in via the arg 'request'
        and then set to variables below.

        Following we create a user by setting the variables passed in the the create_user function
        below and then we save it to our database.

        Args:
            'request' - the values passed in as string via the $http call from register-ctrl of login.html
    '''

    # data = imported json and using the .loads() function, passed in the
    # argument - the decoded body of the request to be posted which is
    # a dictionary of the info typed into the form. Data is the same as data
    # in the register-ctrl $http call.
    data = json.loads(request.body.decode())

    # ASSIGNS CORRESPONDING OBJ VALUE TO A VARIABLE
    username =  data['username']
    password = data['password']
    email = data['email']
    first_name = data['first_name']
    last_name = data['last_name']

    # CALLS CREATE USER FUNCTION ON USER.OBJECTS
    user = User.objects.create_user(
                                    username=username,
                                    password=password,
                                    email=email,
                                    first_name=first_name,
                                    last_name=last_name,
                                    )

    # SAVES USER DATA THAT WAS JUST POSTED
    user.save()

    currentUser = authenticate(username=username, password=password)

    if currentUser is not None:
        return HttpResponseRedirect('/')
    else:
        return Http404


def login_user(request):
    data = json.loads(request.body.decode())

    username = data['username']
    password = data['password']

    user = authenticate(username=username, password=password)

    if user is not None:
        return HttpResponseRedirect('/')
    else:
        return Http404

# CREATE Event #
# @csrf_exempt
def create_event_object(request):
    '''
        Function to create event creation.
        Upon form submission, the values of the fields are passed in via the arg 'request'
        and then set to variables below.

        Following we create an event by setting the variables passed in the the create_event function
        below and then we save it to our database.


def create_new_venue(request):
    '''
        Function to create a new venue.
        Upon form submition, the values of the fields are passed in via the arg 'request'
        and then set to variables below.

        Following we create a venue by setting the variables passed in the the create_new_venue function
        below and then we save it to our database.

        Args:
            'request' - the values passed in as string via the $http call from venue-ctrl
    '''

    # data = imported json and using the .loads() function, passed in the
    # argument - the decoded body of the request to be posted which is
    # a dictionary of the info typed into the form. Data is the same as data
    # in the register-ctrl $http call.
    data = json.loads(request.body.decode())

    # ASSIGNS CORRESPONDING OBJ VALUE TO A VARIABLE
    event_name =  data['event_name']
    event_date = data['event_date']
    event_price = data['event_price']
    event_attendee_capacity = data['event_attendee_capacity']

    # CALLS CREATE USER FUNCTION ON EVENT.OBJECTS
    event = Event.objects.create(
                                    event_name=event_name,
                                    event_date=event_date,
                                    event_price=event_price,
                                    event_attendee_capacity=event_attendee_capacity,
                                    )

    # SAVES EVENT DATA THAT WAS JUST POSTED
    # not sure if we need below line
    event.event()


    venue_name =  data['venue_name']
    seating_capacity = data['seating_capacity']

    # NOT SURE BELOW - CALLS CREATE USER FUNCTION ON VENUE.OBJECTS
    venue = Venue.objects.create(venue_name=venue_name, seating_capacity=seating_capacity)

    # SAVES NEW VENUE DATA THAT WAS JUST POSTED
    venue.save()


    if venue is not None:
        return HttpResponseRedirect('/')
    else:
        return Http404



def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')



def show_all_events(request):
    '''
        Gives all events to angular to be rendered

        Args:
            request - is the database table of events
    '''
    events = Event.objects.all()
    data = serializers.serialize('json', events)
    return HttpResponse(data, content_type='application/json')


def show_all_venues(request):
    '''
        Gives all venues to angular to be rendered
        Args:
          request - is the database table of venues
    '''
    venues = Venue.objects.all()
    data = serializers.serialize('json', venues)
    return HttpResponse(data, content_type='application/json')

