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

    def validate(self, data):
        if data['check_in'] >= data['check_out']:
            raise serializers.ValidationError({"check_out": "check_out must occur after check_in"})
        return data
