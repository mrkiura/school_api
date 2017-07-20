"""Serializers for the API models."""

from rest_framework import serializers
from .models import School, Student

class SchoolSerializer(serializers.ModelSerializer):
    """Serializing the School model."""

    class Meta:
        fields = '__all__' 
        model = School


class StudentSerializer(serializers.ModelSerializer):
    """Serializing the Student model."""

    class Meta:
        fields = '__all__'
        model = Student