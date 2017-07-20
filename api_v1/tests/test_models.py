"""Test cases for the API model"""

from api_v1.models import School, Student
from rest_framework.test import APITestCase
import datetime


class SchoolTest(APITestCase):
    def test_school_creation(self):
        """Test creating a school object"""
        school = School.objects.create(
            name='Shule', email='shule@ymail.com', 
            category='DISTRICT', school_type='BOARDING',
            gender='MIXED')
        self.assertEqual(1, School.objects.count())
        self.assertEqual(school.name, 'Shule')


class StudentTest(APITestCase):
    def setUp(self):
        self.school = School.objects.create(
            name='Shule', email='shule@ymail.com', 
            category='DISTRICT', school_type='BOARDING',
            gender='MIXED')
    def test_student_creation(self):
        """Test creating a student object."""
        student = Student.objects.create(
            name='Masha', date_of_birth=datetime.datetime.today(),
            school=self.school, class_level=4, gender='female'
        )
        self.assertEqual(1, Student.objects.count())
        self.assertEqual(student.gender, 'female')