from django.shortcuts import render
from rest_framework import viewsets
from user.repositories.user_repository import UserRepository
from user.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = UserRepository.get_all()
    serializer_class = UserSerializer
