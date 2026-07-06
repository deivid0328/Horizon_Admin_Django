from django.test import TestCase
from django.urls import reverse

from apps.pqr.models import PQR


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


class PQRViewTest(TestCase):
    def setUp(self):
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

    def test_detalle_pqr(self):
        response = self.client.get(reverse("pqr_detail", args=[self.pqr.id]))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.pqr.title)

    def test_eliminar_pqr(self):
        response = self.client.post(reverse("pqr_delete", args=[self.pqr.id]), follow=True)

        self.assertRedirects(response, reverse("pqr_list"))
        self.assertFalse(PQR.objects.filter(pk=self.pqr.pk).exists())
