# models.py
from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    course_name = models.CharField(max_length=255)
    fee = models.IntegerField()

class Student(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    student_name = models.CharField(max_length=255)
    email = models.EmailField()
    student_age = models.IntegerField(default=0)
    joining_date = models.DateField()
class UserMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=255)
    age = models.IntegerField()
    number = models.CharField(max_length=15)
    image = models.ImageField(upload_to='image/', null=True, blank=True)

