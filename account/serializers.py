from rest_framework.serializers import ModelSerializer
from .models import *


class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'roles')

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            roles=validated_data.get('roles', 3),
            phone_number=validated_data['phone_number']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user