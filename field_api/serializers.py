from rest_framework import serializers
from .models import FieldModel, BookingModel


class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldModel
        fields = ('name', 'owner', 'location', 'capacity', 'description', 'is_indoor', 'created_at', 'updated_at')


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingModel
        fields = ('field', 'user', 'data', 'start_time', 'end_time', 'is_approved')
