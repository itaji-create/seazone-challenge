from django.db import models
from .utils import gerar_hash


class Properties(models.Model):
    code = models.CharField(max_length=30, unique=True)
    guest_limit = models.IntegerField()
    bathrooms = models.IntegerField()
    pets = models.BooleanField()
    activation_date = models.DateField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)


class Adverts(models.Model):
    property = models.ForeignKey(Properties, on_delete=models.CASCADE)
    platform_name = models.TextField()
    platform_fee = models.DecimalField(decimal_places=2, max_digits=6)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)


class Reservations(models.Model):
    code = models.CharField(
        max_length=30,
        editable=False,
        default=gerar_hash,
        unique=True
    )
    ad_belongs = models.ForeignKey(Adverts, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    price = models.DecimalField(decimal_places=2, max_digits=6)
    comments = models.TextField()
    guests_number = models.IntegerField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
