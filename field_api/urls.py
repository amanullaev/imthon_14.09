from django.urls import path
from . import views

urlpatterns = [
    path('filters/', views.FieldFilterView.as_view()),
    path('field_api/', views.FieldListView.as_view(), name='field-list'),
    path('fields/<int:pk>/', views.FieldDetailView.as_view(), name='field-detail'),
    path('bookings/', views.BookingListView.as_view(), name='booking-list'),
    path('bookings/<int:pk>/', views.BookingDetailView.as_view(), name='booking-detail'),

]
