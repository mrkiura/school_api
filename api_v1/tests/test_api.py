"""API tests for School CRUD API"""

from rest_framework.test import APITestCase
from rest_framework import status


class SchoolAPITest(APITestCase):
    def test_school_creation(self):
        """Test creating a school."""
        response = self.client.post(
            '/api/v1/schools',
            {'name': 'BrookHouse', 'email': 'brookhouse@gmail.com',
             'category': 'DISTRICT', 'school_type': 'DAY',
             'gender': 'MIXED'})
        self.assertEqual(response, status.HTTP_201_CREATED)
            