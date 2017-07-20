"""API implementation using viewsets."""

from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .serializers import SchoolSerializer, StudentSerializer
from .models import School, Student


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permissions = (AllowAny,)


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permissions = (AllowAny,)    