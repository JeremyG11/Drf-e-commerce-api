from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import CustomUser as User
from .serializers import UserSerializer 
# Create your views here.


class UserListView(generics.ListCreateUpdateDestroyAPIView):
    """
    List all users, or create a new user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
