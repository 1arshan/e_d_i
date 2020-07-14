from django.db import models
from django.contrib.auth.models import User
from django_better_admin_arrayfield.models.fields import ArrayField


def renaming_uploaded_file1(instance, filename):
    return "profile_pic/" + str(instance.phone_number) + "_" + filename


class StudentProfile(models.Model):
    photo = models.ImageField(upload_to=renaming_uploaded_file1, blank=True)
    standard_or_class = models.CharField(max_length=10)
    email_verified = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pincode = models.CharField(max_length=12)
    date = models.DateTimeField(auto_now=True)
    otp = models.CharField(max_length=8, blank=True)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=13, unique=True, primary_key=True)
    course_field = models.CharField(max_length=20, blank=True)


class TeacherProfile(models.Model):
    photo = models.ImageField(upload_to=renaming_uploaded_file1, blank=True)
    teacher_description = models.TextField(blank=True)
    email_verified = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    otp = models.CharField(max_length=8, blank=True)
    is_verified = models.BooleanField(default=False)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.EmailField(unique=True, blank=True)
    phone_number = models.CharField(max_length=13, unique=True, primary_key=True)
    subject = ArrayField(models.CharField(max_length=20, blank=True), blank=True)
    max_qualification = models.CharField(max_length=50)
    experience = models.CharField(max_length=100, blank=True)

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
    course_field = models.CharField(max_length=20, blank=True)


class TempTeacher(models.Model):
    first_name = models.CharField(max_length=12)
    last_name = models.CharField(max_length=12)
    phone_number = models.CharField(max_length=13, unique=True)
    email = models.EmailField()
    description = models.TextField(blank=True)
    password = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now=True)
    otp = models.CharField(max_length=8, blank=True)
    subject = ArrayField(models.CharField(max_length=20, blank=True), blank=True)
    max_qualification = models.CharField(max_length=50)
    experience = models.CharField(max_length=100, blank=True)
