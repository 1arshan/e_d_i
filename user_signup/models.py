from django.db import models
from django.contrib.auth.models import User


class StudentProfile(models.Model):
    standard_or_class = models.CharField(max_length=10)
    email_verified = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    pincode = models.CharField(max_length=12)
    date = models.DateTimeField(auto_now=True)
    otp = models.CharField(max_length=8, blank=True)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=13, unique=True)


class TeacherProfile(models.Model):
    teacher_description = models.TextField(blank=True)
    email_verified = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    otp = models.CharField(max_length=8, blank=True)
    # subject = ArrayField(models.CharField(max_length=50, blank=True), blank=True, null=True)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.EmailField(unique=True, blank=True)
    phone_number = models.CharField(max_length=13, unique=True, primary_key=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class TempStudent(models.Model):
    first_name = models.CharField(max_length=12)
    last_name = models.CharField(max_length=12)
    phone_number = models.CharField(max_length=13, unique=True)
    email = models.EmailField(blank=True)
    pincode = models.CharField(max_length=10)
    standard_or_class = models.CharField(max_length=10)
    password = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now=True)
    otp = models.CharField(max_length=8, blank=True)


class TempTeacher(models.Model):
    first_name = models.CharField(max_length=12)
    last_name = models.CharField(max_length=12)
    phone_number = models.CharField(max_length=13, unique=True)
    email = models.EmailField(unique=True)
    description = models.TextField(blank=True)
    password = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now=True)
    otp = models.CharField(max_length=8, blank=True)


# subject = ArrayField(models.CharField(max_length=50, blank=True), blank=True, null=True)
"""
class TeacherSubject(models.Model):
    teacher_link =models.ForeignKey(TempTeacher,on_delete=models.CASCADE)"""
