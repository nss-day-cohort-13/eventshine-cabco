from django.conf.urls import url

from . import views

app_name = "cabco_project"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login_user, name='login_user'),
    url(r'^register/$', views.create_user_object, name='create_user_object'),
    url(r'^new_venue/$', views.create_new_venue, name='create_new_venue'),
]
