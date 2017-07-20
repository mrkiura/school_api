"""API tests for School CRUD API"""

from rest_framework.test import APITestCase
from rest_framework import status


class SchoolAPITest(APITestCase):
    def test_school_creation(self):
        """Test creating a school."""
        response = self.client.post(
            '/api/v1/schools/',
            {'name': 'BrookHouse', 'email': 'brookhouse@gmail.com',
             'category': 'dist', 'school_type': 'day',
             'gender': 'mixed'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            