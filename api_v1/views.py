"""API implementation using viewsets."""

from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .serializers import SchoolSerializer, StudentSerializer
from .models import School


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permissions = (AllowAny,)