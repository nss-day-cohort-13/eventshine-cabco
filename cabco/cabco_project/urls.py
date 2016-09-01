from django.conf.urls import url

from . import views

app_name = "cabco_project"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login_user, name='login_user'),
    url(r'^register/$', views.create_user_object, name='create_user_object'),
    url(r'^new-event/$', views.create_event_object, name='create_event_object'),
    url(r'^events/$', views.show_all_events, name='show_all_events'),
    url(r'^venues/$', views.show_all_venues, name='show_all_venues'),
    url(r'^tickets/$', views.show_all_tickets, name='show_all_tickets'),
    url(r'^new_venue/$', views.create_new_venue, name='create_new_venue'),
    url(r'^logout/$', views.logout_view, name='logout_view'),
]
