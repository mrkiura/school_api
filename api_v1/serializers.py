"""Serializers for the API models."""

from rest_framework import serializers
from .models import School, Student



class StudentSerializer(serializers.ModelSerializer):
    """Serializing the Student model."""

    class Meta:
        fields = '__all__'
        model = Student


class SchoolSerializer(serializers.ModelSerializer):
    """Serializing the School model."""

    students = StudentSerializer(many=True, read_only=True)
    class Meta:
        fields =  ('name', 'email', 'school_type', 'gender', 'category', 'students')
        model = School