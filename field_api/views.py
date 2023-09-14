from .models import FieldModel, BookingModel
from .serializers import FieldSerializer, BookingSerializer
from account.permissions import AdminPermission, OwnerPermission, UserPermission
from rest_framework import generics
from rest_framework import filters
from django.db.models import Q
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class FieldListView(generics.ListCreateAPIView):
    queryset = BookingModel.objects.all()
    serializer_class = FieldSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['booked_time']

    def get_queryset(self):
        start_time = self.request.query_params.get('start_time')
        end_time = self.request.query_params.get('end_time')
        date = self.request.query_params.get('date')

        queryset = BookingModel.objects.all()

        if start_time and end_time:
            queryset = queryset.filter(
                Q(booked_time__lt=start_time) | Q(booked_time__gt=end_time) | Q(booked_time__isnull=True)
            )

        if date:
            queryset = queryset.filter(data=date)

        return queryset


# class FieldDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = FieldModel.objects.all()
#     serializer_class = FieldSerializer
#     permission_classes = [UserPermission]


class BookingListView(generics.ListCreateAPIView):
    queryset = BookingModel.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [UserPermission]


class BookingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookingModel.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [OwnerPermission]


class CreateStadiomView(generics.CreateAPIView):
    queryset = FieldModel.objects.all()
    serializer_class = FieldSerializer
    permission_classes = (OwnerPermission,)


class GetAllStadiomView(generics.ListAPIView):
    queryset = FieldModel.objects.all()
    serializer_class = FieldSerializer
    permission_classes = (UserPermission,)


class DetailStadiomView(APIView):
    def get(self, request, *args, **kwargs):
        st = get_object_or_404(FieldModel, id=kwargs['id'])
        serializers = FieldSerializer(st)
        permission_classes = (UserPermission,)
        return Response(serializers.data)


class UpdateStadiomView(APIView):
    def patch(self, request, *args, **kwargs):
        st = get_object_or_404(FieldModel, id=kwargs['id'])
        serializer = FieldSerializer(st, data=request.data, partial=True)
        permission_classes = (AdminPermission,)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class DeleteStadiomView(APIView):
    def delete(self, request, *args, **kwargs):
        permission_classes = (AdminPermission,)
        st = get_object_or_404(FieldModel, id=kwargs['id'])
        st.delete()
        return Response({'msg':'deleted'})


class DeleteBookings(APIView):
    def delete(self, request, *args, **kwargs):
        permission_classes = (AdminPermission,)
        st = get_object_or_404(BookingModel, id=kwargs['id'])
        st.delete()
        return Response({'msg':'deleted'})


class ListBookByTimeAPIView(generics.ListAPIView):
    queryset = BookingModel.objects.all()
    serializer_class = BookingSerializer
    permission_classes = (OwnerPermission,)

    def get_queryset(self):
        # user = self.request.user
        # author = AuthorModel.objects.get(user=user)
        # return BookModel.objects.filter(author=author.id)
        book = BookingModel.objects.all()
        if self.request.date != book.date:
            if self.request.start_time != book.start_time:
                if self.request.end_time != book.end_time:
                    return FieldSerializer
