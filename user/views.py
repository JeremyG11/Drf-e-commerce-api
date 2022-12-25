from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import CustomUser as User
from .serializer import UserSerializer 
# Create your views here.


class UserListView(generics.ListCreateUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
