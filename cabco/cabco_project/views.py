from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Event, Venue
from django.template import RequestContext

from django.contrib.auth.models import User

# from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    """
    This class is for our Index.
    """
    template_name = 'index.html'
    return render(request, template_name, {})


# VIEWS CATCH 'POST'  <-----LOOK AT THAT, WOW.


# CREATE USER #
@csrf_exempt
def create_user_object(request):
    print(request)
    '''
        Function to catch registration of user from login.html.
        Upon form submition, the values of the fields are passed in via the arg 'request'
        and then set to variables below.

        Following we create a user by setting the variables passed in the the create_user function
        below and then we save it to our database.

        Args:
            'request' - the values passed in as string via the form of login.html
    '''

    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']

    user = User.objects.create_user(
                                    username=username,
                                    password=password,
                                    email=email,
                                    first_name=first_name,
                                    last_name=last_name,
                                    )

    user.save()

# user creation view

# user login view

# create event view

# create venue view
