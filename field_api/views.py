from .models import FieldModel, BookingModel
from .serializers import FieldSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework import filters
from django.db.models import Q
from datetime import datetime
from account.permissions import OwnerPermission, UserPermission


class FieldListView(generics.ListCreateAPIView):
    queryset = FieldModel.objects.all()
    serializer_class = FieldSerializer


class FieldDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FieldModel.objects.all()
    serializer_class = FieldSerializer
    permission_classes = (OwnerPermission, UserPermission)


class BookingListView(generics.ListCreateAPIView):
    queryset = BookingModel.objects.all()
    serializer_class = BookingSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['booked_time']

    def get_queryset(self):
        start_time_str = self.request.query_params.get('start_time')
        end_time_str = self.request.query_params.get('end_time')
        date_str = self.request.query_params.get['date']

        queryset = BookingModel.objects.all()

        if start_time_str and end_time_str:
            try:
                start_time = datetime.fromisoformat(start_time_str)
                end_time = datetime.fromisoformat(end_time_str)
            except ValueError:
                return queryset

            queryset = queryset.filter(
                Q(booked_time__lt=start_time) | Q(booked_time__gt=end_time) | Q(booked_time__isnull=True)
            )

        if date_str:
            try:
                date = datetime.fromisoformat(date_str).date()
            except ValueError:
                return queryset

            queryset = queryset.filter(date=date)

        return queryset


class BookingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookingModel.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [OwnerPermission, UserPermission]
