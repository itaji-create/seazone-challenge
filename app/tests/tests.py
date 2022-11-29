import json
from django.test import TestCase, client


from app.models import Properties, Adverts, Reservations


class TestStatusCodeRequests(TestCase):
    def setUp(self):
        self.client = client.Client()

        self.data = {
            "code": "codigo",
            "guest_limit": 2,
            "bathrooms": 2,
            "pets": True,
            "activation_date": "2022-10-01",
        }

        self.res = self.client.post(
            "/properties/",
            content_type="application/json",
            data=json.dumps(self.data)
        )

        self.properties = json.loads(self.res.content)

    def test_requests_get_all_routes(self):
        self.assertEquals(self.client.get('/properties/').status_code, 200)
        self.assertEquals(self.client.get('/properties/1/').status_code, 200)
        self.assertEquals(self.client.get('/adverts/').status_code, 200)
        self.assertEquals(self.client.get('/reservations/').status_code, 200)

    def test_create_property(self):
        self.assertEquals(self.res.status_code, 201)
        assert self.properties["code"] == self.data["code"]
        assert self.properties["guest_limit"] == self.data["guest_limit"]
        assert self.properties["bathrooms"] == self.data["bathrooms"]
        assert self.properties["pets"] == self.data["pets"]

    def test_update_property(self):
        res = self.client.patch(
            "/properties/1/",
            content_type='application/json',
            data=json.dumps({
                "code": "novo-codigo",
            }))

        self.assertEqual(res.status_code, 200)
        assert json.loads(res.content)["code"] == "novo-codigo"

    def test_delete_property(self):
        res = self.client.delete('/properties/1/')
        self.assertEqual(res.status_code, 204)
        self.assertEquals(self.client.get('/properties/1/').status_code, 404)


class TestClass(TestCase):
    def setUpTestData():
        Properties.objects.create(
            code="50001",
            guest_limit=1,
            bathrooms=1,
            pets=True,
            activation_date="2010-10-10"
        )

        Adverts.objects.create(
            property=Properties.objects.get(id=1),
            platform_name='book',
            platform_fee=10,
        )

        Reservations.objects.create(
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
