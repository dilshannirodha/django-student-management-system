from django.db import models

# Create your models here.

class Student(models.Model):
    regnumber = models.SlugField(max_length=100, unique=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    nic = models.CharField(max_length=12)

    GENDER_CHOICES = [
        ('male','male'),
        ('female', 'female'),
    ]
    
    gender = models.CharField(
        max_length=6,
        choices=GENDER_CHOICES,
        default='male',
    )