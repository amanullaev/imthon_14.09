from rest_framework import serializers
from .models import BornModel
class BornSerializer(serializers.ModelSerializer):
    class Meta:
        model = BornModel
        fields = ['id', 'title', 'time', 'is_booked']