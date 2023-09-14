from .models import FieldModel, BookingModel
from .serializers import FieldSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework import filters
from rest_framework.views import APIView
from django.db.models import Q
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from datetime import datetime


class FieldFilterView(APIView):
    def get(self, request):
        day = request.query_params.get('day', '2023-09-14')
        print(day)
        data = datetime.strptime(day, '%Y-%m-%d').date()
        todos = FieldModel.objects.filter(created_at__date=data,)
        serializer = FieldSerializer(todos, many=True)
        return Response(serializer.data)



class FieldListView(generics.ListCreateAPIView):
    queryset = BookingModel.objects.all()
    serializer_class = FieldSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['booked_time']

    def get_queryset(self):
        start_time = self.request.query_params.get('start_time')
        end_time = self.request.query_params.get('end_time')
        date = self.request.query_params.get('day')

        queryset = BookingModel.objects.all()

        if start_time and end_time:
            queryset = queryset.filter(
                Q(booked_time__lt=start_time) | Q(booked_time__gt=end_time) | Q(booked_time__isnull=True)
            )

        if date:
            queryset = queryset.filter(day=date)

        return queryset


class FieldDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FieldModel.objects.all()
    serializer_class = FieldSerializer
    permission_classes = [IsAuthenticated]


class BookingListView(generics.ListCreateAPIView):
    queryset = BookingModel.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]


class BookingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookingModel.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
