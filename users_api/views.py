from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import UserSerializer, HomeSerializer, PhotoSerializer
from .models import User, Home, Photo
from rest_framework.decorators import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework import serializers

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = UserSerializer # tell django what serializer to use

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer


class HomeList(generics.ListCreateAPIView):
    queryset = Home.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = HomeSerializer # tell django what serializer to use

class HomeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Home.objects.all().order_by('id')
    serializer_class = HomeSerializer


class PhotoList(generics.ListCreateAPIView):
    queryset = Photo.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = PhotoSerializer # tell django what serializer to use

class PhotoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Photo.objects.all().order_by('id')
    serializer_class = PhotoSerializer

CurUser = get_user_model()

class CurUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurUser
        fields = ('id', 'username')


class LoggedInUserView(APIView):
    def get(self, request):
        serializer = CurUserSerializer(request.user)
        return Response(serializer.data)
