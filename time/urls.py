from django.urls import path
from .views import  BornView

urlpatterns = [
    path('events/', BornView.as_view(), name='events_endpoint'),
]