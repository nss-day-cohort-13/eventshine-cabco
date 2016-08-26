from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
class Index(TemplateView):
  """
  This class is for our Index.
  """
    template_name = 'index.html'
