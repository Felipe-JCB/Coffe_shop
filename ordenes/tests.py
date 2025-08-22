from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class MyOrderViewTests(TestCase):

    def test_no_logged_user_should_redirect(self):
        url = reverse("mi_orden")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/usuarios/login/?next=/pedidos/mi-orden")

    def test_logged_user_should_redirect(self):
        url = reverse("mi_orden")
        user = get_user_model().objects.create(username="test")
        self.client.force_login(user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)