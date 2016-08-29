from django.conf.urls import url

from . import views

app_name = "cabco_project"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.create_user_object, name='create_user_object'),
]
