from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import PropertiesViewSet, AdvertsViewSet, ReservationsViewSet


router = routers.DefaultRouter()

router.register('properties', PropertiesViewSet)
router.register('adverts', AdvertsViewSet)
router.register('reservations', ReservationsViewSet)

urlpatterns = [
    path('', include(router.urls))
]