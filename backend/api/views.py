from django.shortcuts import render
from rest_framework import generics
from .models import Conference
from .serializers import  ConferenceSerializer

class GetAll(generics.ListAPIView):
    queryset = Conference.objects.all()
    serializer_class = ConferenceSerializer

class GetOne(generics.RetrieveAPIView):
    queryset = Conference.objects.all()
    serializer_class = ConferenceSerializer
    lookup_field = 'slug'