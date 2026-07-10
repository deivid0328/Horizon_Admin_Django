from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from apps.pqr.models import PQR
from apps.reservations.models import Reservation


class PQRModelTest(TestCase):
    def test_create_pqr(self):
        pqr = PQR.objects.create(
            title="Daño ascensor",
            description="El ascensor no funciona",
            status="open",
        )

        self.assertEqual(pqr.title, "Daño ascensor")
        self.assertEqual(pqr.status, "open")
        self.assertEqual(str(pqr), "Daño ascensor")


class LandingLoginTest(TestCase):
    def test_landing_login_with_valid_email_redirects_to_pqr(self):
        response = self.client.post(
            reverse("landing_login"),
            {"email": "demo@horizon.com", "password": "cualquier-password"},
            follow=True,
        )

        self.assertRedirects(response, reverse("pqr_list"))
        self.assertTrue(get_user_model().objects.filter(email="demo@horizon.com").exists())
        self.assertTrue(response.wsgi_request.user.is_authenticated)


class PQRViewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="admin",
            email="admin@horizon.com",
            password="123456",
        )
        self.client.force_login(self.user)
        self.pqr = PQR.objects.create(
            title="Fuga de agua",
            description="Hay fuga en el baño",
            status="process",
        )

    def test_listado_pqr(self):
        response = self.client.get(reverse("pqr_list"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pqr/pqr_list.html")
        self.assertContains(response, self.pqr.title)

    def test_crear_pqr_via_formulario(self):
        response = self.client.post(
            reverse("pqr_create"),
            {
                "title": "Incidencia de luz",
                "description": "La luz del pasillo falla",
                "status": "open",
            },
            follow=True,
        )

        self.assertRedirects(response, reverse("pqr_list"))
        self.assertTrue(PQR.objects.filter(title="Incidencia de luz").exists())

    def test_dashboard_incluye_metricas_utiles(self):
        Reservation.objects.create(
            resident_name="Ana García",
            area="salon",
            reservation_date="2026-07-15",
            start_time="10:00",
            end_time="12:00",
            status="approved",
        )

        response = self.client.get(reverse("dashboard"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pqr/dashboard.html")
        self.assertContains(response, "Resumen general")
        self.assertContains(response, "PQR abiertas")
        self.assertContains(response, "Reservas aprobadas")

    def test_pqr_list_muestra_solo_la_lista(self):
        response = self.client.get(reverse("pqr_list"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pqr/pqr_list.html")
        self.assertContains(response, "Gestión de PQR")
        self.assertNotContains(response, "Resumen general")

    def test_logout_redirige_al_login(self):
        self.client.force_login(self.user)

        response = self.client.post(reverse("logout"), follow=True)

        self.assertRedirects(response, reverse("landing_login"))
        self.assertFalse(response.wsgi_request.user.is_authenticated)

    def test_detalle_pqr(self):
        response = self.client.get(reverse("pqr_detail", args=[self.pqr.id]))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.pqr.title)

    def test_eliminar_pqr(self):
        response = self.client.post(reverse("pqr_delete", args=[self.pqr.id]), follow=True)

        self.assertRedirects(response, reverse("pqr_list"))
        self.assertFalse(PQR.objects.filter(pk=self.pqr.pk).exists())
