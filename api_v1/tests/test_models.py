from api_v1.models import School
from rest_framework.test import APITestCase


class SchoolTest(APITestCase):
    def test_school_creation(self):
        school = School.objects.create(
            name='Shule', email='shule@ymail.com', 
            category='DISTRICT', school_type='BOARDING',
            gender='MIXED')
        self.assertEqual(1, School.objects.count())
        self.assertEqual(school.name, 'Shule')