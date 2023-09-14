from django.urls import path
from . import views

urlpatterns = [
    path('field_api/', views.FieldListView.as_view(), name='field-list'),
    path('fields/<int:pk>/', views.FieldDetailView.as_view(), name='field-detail'),
    path('bookings/<str:date>/', views.BookingListView.as_view(), name='booking-list'),
    path('bookings/<int:pk>/', views.BookingDetailView.as_view(), name='booking-detail'),

]
