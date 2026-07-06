from datetime import date, time

from django.test import TestCase
from django.urls import reverse

from apps.reservations.models import Reservation


class ReservationModelTest(TestCase):
    def test_create_reservation(self):
        reservation = Reservation.objects.create(
            resident_name="Ana Pérez",
            area="salon",
            reservation_date=date(2026, 7, 10),
            start_time=time(14, 0),
            end_time=time(16, 0),
            status="pending",
        )

        self.assertEqual(reservation.resident_name, "Ana Pérez")
        self.assertEqual(reservation.area, "salon")
        self.assertEqual(str(reservation), "Ana Pérez - salon")


class ReservationViewTest(TestCase):
    def setUp(self):
        self.reservation = Reservation.objects.create(
            resident_name="Carlos Gómez",
            area="pool",
            reservation_date=date(2026, 7, 12),
            start_time=time(10, 0),
            end_time=time(12, 0),
            status="approved",
        )

    def test_listado_reservations(self):
        response = self.client.get(reverse("reservation_list"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "reservations/reservation_list.html")
        self.assertContains(response, self.reservation.resident_name)

    def test_crear_reservation_via_formulario(self):
        response = self.client.post(
            reverse("reservation_create"),
            {
                "resident_name": "Luisa Torres",
                "area": "court",
                "reservation_date": "2026-07-15",
                "start_time": "18:00",
                "end_time": "20:00",
                "status": "pending",
            },
            follow=True,
        )

        self.assertRedirects(response, reverse("reservation_list"))
        self.assertTrue(Reservation.objects.filter(resident_name="Luisa Torres").exists())

    def test_detalle_reservation(self):
        response = self.client.get(reverse("reservation_detail", args=[self.reservation.id]))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.reservation.resident_name)

    def test_eliminar_reservation(self):
        response = self.client.post(reverse("reservation_delete", args=[self.reservation.id]), follow=True)

        self.assertRedirects(response, reverse("reservation_list"))
        self.assertFalse(Reservation.objects.filter(pk=self.reservation.pk).exists())
