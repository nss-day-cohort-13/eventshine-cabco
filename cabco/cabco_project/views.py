from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.generic import TemplateView
from .models import Event, Venue, Ticket
from django.template import RequestContext
import json
from django.core import serializers
from django.contrib.auth import logout, login

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
        login(request, currentUser)
        return HttpResponseRedirect('/')
    else:
        return Http404


def login_user(request):
    data = json.loads(request.body.decode())

    username = data['username']
    password = data['password']

    user = authenticate(username=username, password=password)
    # login(user)

    if user is not None:
        login(request, user)
        # print('login user', request.user)
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
    '''
    # data = imported json and using the .loads() function, passed in the
    # argument - the decoded body of the request to be posted which is
    # a dictionary of the info typed into the form. Data is the same as data
    # in the register-ctrl $http call.
    data = json.loads(request.body.decode())

    print('event_creator', request.user)

    # ASSIGNS CORRESPONDING OBJ VALUE TO A VARIABLE
    event_name =  data['event_name']
    description = data['description']
    city = data['city']
    # event_date = data['event_date']
    begin_date_time = data['begin_date_time']
    end_date_time = data['end_date_time']
    atendee_limit = data['atendee_limit']
    event_price = data['event_price']
    event_creator = request.user
    event_venue = data['event_venue']

    event_venue = Venue.objects.get(pk=event_venue)


    # CALLS CREATE USER FUNCTION ON EVENT.OBJECTS
    event = Event.objects.create(
                                    event_name=event_name,
                                    description=description,
                                    city=city,
                                    begin_date_time=begin_date_time,
                                    end_date_time=end_date_time,
                                    atendee_limit=atendee_limit,
                                    event_price=event_price,
                                    event_creator=event_creator,
                                    event_venue = event_venue
                                    )

    # SAVES NEW VENUE DATA THAT WAS JUST POSTED
    event.save()


    if event is not None:
        return HttpResponseRedirect('/')
    else:
        return Http404



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

def create_new_ticket(request):

    data = json.loads(request.body.decode())

    user = request.user
    event = data['event_pk']

    event = Event.objects.get(pk=event)

    print('user', user)
    print('event', event)

    ticket = Ticket.objects.create(user=user, event=event)

    ticket.save()

    if ticket is not None:
        return HttpResponseRedirect('/')
    else:
        return Http404


def logout_view(request):
    logout(request)
    print('user', request.user)
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

# def show_all_tickets(request):
#     '''
#         Gives all tickets to angular to be rendered
#         Args:
#             request - is the database table of tickets
#     '''
#     tickets = Ticket.objects.all()
#     data = serializers.serialize('json', tickets)
#     return HttpResponse(data, content_type='application/json')

def get_ticket_count(request):
    data = json.loads(request.body.decode())
    event=data['event_pk']

    eventTickets = Ticket.objects.filter(event=event).count()
    # eventTicketData = serializers.serialize('json', eventTickets)
    return HttpResponse(eventTickets, content_type='application/json')
