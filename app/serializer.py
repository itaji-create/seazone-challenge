from .models import Properties, Adverts, Reservations
from rest_framework import serializers

class PropertiesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Properties
        fields = '__all__'


class AdvertsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Adverts
        fields = '__all__'


class ReservationsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reservations
        fields = '__all__'
