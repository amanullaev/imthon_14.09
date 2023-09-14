from rest_framework import generics
from .models import FieldModel, BookingModel
from .serializers import FieldSerializer, BookingSerializer
from config.permissions import AdminPermission, OwnerPermission, UserPermission
from rest_framework import generics
from rest_framework import filters
from django.db.models import Q


class FieldListView(generics.ListAPIView):
    queryset = FieldModel.objects.all()
    serializer_class = FieldSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['booked_time']

    def get_queryset(self):
        start_time = self.request.query_params.get('start_time')
        end_time = self.request.query_params.get('end_time')

        if start_time and end_time:
            return FieldModel.objects.filter(
                Q(booked_time__lt=start_time) | Q(booked_time__gt=end_time) | Q(booked_time__isnull=True)
            )
        else:
            return FieldModel.objects.filter(booked_time__isnull=True)


class FieldDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FieldModel.objects.all()
    serializer_class = FieldSerializer
    permission_classes = [UserPermission]


class BookingListView(generics.ListCreateAPIView):
    queryset = BookingModel.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [UserPermission]


class BookingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookingModel.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [UserPermission, OwnerPermission]
