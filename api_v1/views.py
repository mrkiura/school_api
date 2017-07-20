"""API views using viewsets."""

from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .serializers import SchoolSerializer, StudentSerializer
from .models import School, Student


class SchoolViewSet(viewsets.ModelViewSet):
    """
    API View that provides CRUD functionality for the School entity.

    URL:
        /api/v1/schools/

    Methods:
        GET, PUT, POST, DELETE
    """

    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permissions = (AllowAny,)


class StudentViewSet(viewsets.ModelViewSet):
    """
    API View that provides CRUD functionality for the Student entity.

    URL:
        /api/v1/students/

    Methods:
        GET, PUT, POST, DELETE
    """

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permissions = (AllowAny,)
