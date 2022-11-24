from django.shortcuts import render
from rest_framework import viewsets
from .models import Properties, Adverts, Reservations
from .serializer import PropertiesSerializer, AdvertsSerializer, ReservationsSerializer


class PropertiesViewSet(viewsets.ModelViewSet):
    queryset = Properties.objects.all()
    serializer_class = PropertiesSerializer


class AdvertsViewSet(viewsets.ModelViewSet):
    queryset = Adverts.objects.all()
    serializer_class = AdvertsSerializer


class ReservationsViewSet(viewsets.ModelViewSet):
    queryset = Reservations.objects.all()
    serializer_class = ReservationsSerializer
