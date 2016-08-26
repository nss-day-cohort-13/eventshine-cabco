from django.conf.urls import url

from . import views

app_name = "cabco_project"
urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^register/$', views.create_user, name='create_user'),
]
