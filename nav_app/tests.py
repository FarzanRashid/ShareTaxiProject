from django.test import TestCase
from django.urls import reverse
from .models import RideRequest
import json
from datetime import datetime


class BookTaxiTestCase(TestCase):
    def test_book_taxi_success(self):
        url = reverse('book_taxi')
        data = {
            'dropoff_location': 'Azimpur',
            'departure_time': '10:00',
            'email': 'test@example.com',
            'pickup_location': 'DMD',
            'date': "2023-04-03"
        }
        response = self.client.post(url, json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(RideRequest.objects.count(), 1)
        self.assertEqual(RideRequest.objects.first().dropoff_location, 'Azimpur')
        self.assertEqual(RideRequest.objects.first().pickup_location, 'DMD')
        departure_time = RideRequest.objects.first().departure_time
        expected_departure_time = datetime.strptime('10:00', '%H:%M').time()
        self.assertEqual(departure_time, expected_departure_time)
        self.assertEqual(RideRequest.objects.first().email, 'test@example.com')
        self.assertEqual(RideRequest.objects.first().date, datetime.strptime('2023-04-03', '%Y-%m-%d').date())

    def test_book_taxi_invalid_method(self):
        url = reverse('book_taxi')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'error': 'Invalid request method'})

    def test_book_taxi_invalid_data(self):
        url = reverse('book_taxi')
        data = {
            'dropoff_location': 'DMD',
            'departure_time': 'invalid',
            'email': 'test@example.com',
            'pickup_location': 'Azimpur',
            'date': "2023-04-03"
        }
        response = self.client.post(url, json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'success': False, 'error': 'Invalid data'})
