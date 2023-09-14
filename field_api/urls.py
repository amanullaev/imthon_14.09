from django.urls import path
from .views import *

urlpatterns = [
    path('field_api/', FieldListView.as_view(), name='field-list'),
    path('fields/<int:pk>/', FieldDetailView.as_view(), name='field-detail'),
    path('bookings/', BookingListView.as_view(), name='booking-list'),
    path('bookings/<int:pk>/', BookingDetailView.as_view(), name='booking-detail'),
    # path('fields/', views.FieldListView.as_view(), name='field-list'),
    path('createstadiom/', CreateStadiomView.as_view()),
    path('getallstadiom/', GetAllStadiomView.as_view()),
    path('get_by_index_stadiom/<int:id>/', DetailStadiomView.as_view()),
    path('update_stadiom/<int:id/', UpdateStadiomView.as_view()),
    path('delete_stadiom/<int:id>/', DeleteStadiomView.as_view()),
    path('delete_book/<int:id>/', DeleteBookings.as_view()),
    path('listbookbytime/', ListBookByTimeAPIView.as_view())
]
