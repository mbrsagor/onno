from rest_framework import permissions
from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import User
from .serializers import (ChangePasswordSerializer, CustomJwtLoginSerializer,
                          UserSerializer, UserUpdateSerializer)


class CreateUserView(CreateAPIView):
    model = User
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer


class UpdateUserView(UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = UserUpdateSerializer


class DetailUserView(RetrieveAPIView):
    queryset = User.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer


class UserLoginView(TokenObtainPairView):
    serializer_class = CustomJwtLoginSerializer


class ChangePasswordView(UpdateAPIView):
    lookup_field = 'pk'
    queryset = User.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ChangePasswordSerializer
