from django.conf.urls import url

from . import views

app_name = "cabco_project"
urlpatterns = [
    url(r'^$', views.index, name='index'),
]
