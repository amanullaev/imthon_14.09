from rest_framework import generics
from .models import UserModel
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from config.permissions import AdminPermission, OwnerPermission, UserPermission


class UserListView(generics.ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = (OwnerPermission,)
