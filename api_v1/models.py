from django.db import models

# Create your models here.
class School(models.Model):
    """Model representing the school entity."""
    type_choices = (
        ('day', 'DAY'),
        ('boarding', 'BOARDING'),
        ('both', 'DAY & BOARDING')
    )
    gender_choices = (
        ('boys', 'BOYS'),
        ('girls', 'GIRLS'),
        ('mixed', 'MIXED')
    )
    category_choices = (
        ('dist', 'DISTRICT'),
        ('national', 'NATIONAL'),
        ('prov', 'PROVINCIAL')
    )
    name = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(max_length=200, blank=True)
    school_type = models.CharField(max_length=15, choices=type_choices, null=False)
    gender = models.CharField(max_length=15, choices=gender_choices, null=False)
    category = models.CharField(max_length=15, choices=category_choices, null=False)

    
class Student(models.Model):
    """Model representing the student entity."""
    gender_choices = (
        ('male', 'MALE'),
        ('female', 'FEMALE'),
        ('other', 'OTHER')
    )
    name = models.CharField(max_length=255, blank=False, null=False)
    date_of_birth = models.DateField()
    school = models.ForeignKey(
        School, related_name='students', on_delete=models.CASCADE)
    class_level = models.IntegerField()
    gender = models.CharField(max_length=6, choices=gender_choices)