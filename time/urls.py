from django.urls import path
from .views import  BornView

urlpatterns = [
    path('born_time/', BornView.as_view(), name='events_endpoint'),
]
