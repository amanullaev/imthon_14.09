from django.urls import path
from .views import *

urlpatterns = [
    path('fields/', FieldListView.as_view(), name='field-list'),
    path('fields/<int:pk>/', FieldDetailView.as_view(), name='field-detail'),
    path('bookings/', BookingListView.as_view()),
    path('bookings/<int:pk>/', BookingDetailView.as_view()),
    path('fields/', FieldListView.as_view(), name='field-list'),
    path('createstadiom/', CreateStadiomView.as_view()),
    path('getallstadiom/', GetAllStadiomView.as_view()),
    path('get_by_index_stadiom/<int:id>/', DetailStadiomView.as_view()),
    path('update_stadiom/<int:id/', UpdateStadiomView.as_view()),
    path('delete_stadiom/<int:id>/', DeleteStadiomView.as_view()),
    path('delete_book/<int:id>/', DeleteBookings.as_view()),
    path('listbookbytime/', ListBookByTimeAPIView.as_view()),
    path('books/',ListBookByTimeView.as_view())
]

# path('detail/<str:date>/<str:start_time>/<str:end_time>', views.Detail.as_view())