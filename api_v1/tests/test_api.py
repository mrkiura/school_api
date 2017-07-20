"""API tests for School CRUD API"""

from rest_framework.test import APITestCase
from rest_framework import status
import datetime


class SchoolAPITest(APITestCase):
    def test_school_creation(self):
        """Test creating a school."""
        response = self.client.post(
            '/api/v1/schools/',
            {'name': 'BrookHouse', 'email': 'brookhouse@gmail.com',
             'category': 'dist', 'school_type': 'day',
             'gender': 'mixed'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class StudentAPITest(APITestCase):
    def setUp(self):
        response = self.client.post(
            '/api/v1/schools/',
            {'name': 'BrookHouse', 'email': 'brookhouse@gmail.com',
             'category': 'dist', 'school_type': 'day',
             'gender': 'mixed'})
        self.school = response.data
        
    def test_student_creation(self):
        """Test creating a student."""
        response = self.client.post(
            '/api/v1/students/',
            {'name': 'Amaka', 'date_of_birth': '1995-07-23',
             'school': str(self.school['id']), 'class_level': 4, 'gender': 'female'
            })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            

        