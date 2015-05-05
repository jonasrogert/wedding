from django.conf.urls import patterns, url
from . import views


urlpatterns = patterns(
    'RsvpForm.views',
    url(r'^', views.RsvpView.as_view(), name='rsvp-form'),
)
