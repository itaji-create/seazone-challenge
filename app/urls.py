from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import PropertiesViewSet, AdvertsViewSet, ReservationsViewSet


router = routers.DefaultRouter()

router.register(r'properties', PropertiesViewSet)
router.register(r'adverts', AdvertsViewSet)
router.register(r'reservations', ReservationsViewSet)

urlpatterns = [
    path('', include(router.urls))
]