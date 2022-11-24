from django.db import models

class Properties(models.Model):
    name = models.CharField(max_length=255)
    guest_limit = models.IntegerField()
    bathrooms = models.IntegerField()
    pets = models.BooleanField()
    activation_date = models.DateField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

class Adverts(models.Model):
    name = models.CharField(max_length=255)
    property = models.ForeignKey(Properties, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    platform_name = models.TextField()
    platform_fee = models.DecimalField(decimal_places=2, max_digits=6)
    update_date = models.DateTimeField(auto_now=True)

class Reservations(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=30)
    ad_belongs = models.ForeignKey(Adverts, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    price = models.DecimalField(decimal_places=2, max_digits=6)
    comments = models.TextField()
    guests_number = models.IntegerField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
