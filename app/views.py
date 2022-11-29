from rest_framework import viewsets


from .models import Properties, Adverts, Reservations
from . import serializer


class PropertiesViewSet(viewsets.ModelViewSet):
    queryset = Properties.objects.all()
    serializer_class = serializer.PropertiesSerializer


class AdvertsViewSet(viewsets.ModelViewSet):
    queryset = Adverts.objects.all()
    serializer_class = serializer.AdvertsSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'head']


class ReservationsViewSet(viewsets.ModelViewSet):
    queryset = Reservations.objects.all()
    serializer_class = serializer.ReservationsSerializer
    http_method_names = ['get', 'post', 'delete', 'head']
