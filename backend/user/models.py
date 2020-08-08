from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20)
    room_number = models.IntegerField()
    hostel_name = models.CharField(max_length=20) 