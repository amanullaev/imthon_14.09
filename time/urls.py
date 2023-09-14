from django.urls import path
from .views import events_endpoint

urlpatterns = [
    path('events/', events_endpoint, name='events_endpoint'),
]