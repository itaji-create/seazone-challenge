from django.test import TestCase


from app.models import Properties, Adverts, Reservations


class TestClass(TestCase):
    @classmethod
    def setUpTestData(self):
        self.properties = Properties.objects.create(
            code="50001",
            guest_limit=1,
            bathrooms=1,
            pets=True,
            activation_date="2010-10-10"
        )

        self.adverts = Adverts.objects.create(
            property=Properties.objects.get(id=1),
            platform_name='book',
            platform_fee=10,
        )

        self.reservations = Reservations.objects.create(
            ad_belongs=Adverts.objects.get(id=1),
            check_in="2022-10-10",
            check_out="2022-11-10",
            price=140.00,
            comments="sem comentários",
            guests_number=2
        )

    def test_code_label(self):
        property = Properties.objects.get(id=1)
        field_label = property.code
        self.assertEquals(field_label, '50001')

    def test_adverts_label(self):
        property = Adverts.objects.get(id=1)
        field_label = property.platform_name
        self.assertEquals(field_label, 'book')

    def test_reservations_label(self):
        property = Reservations.objects.get(id=1)
        field_label = property.comments
        self.assertEquals(field_label, 'sem comentários')
