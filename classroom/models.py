from django.db import models
from user_signup.models import TeacherProfile


class Institute(models.Model):
    name = models.CharField(max_length=60)
    pincode = models.CharField(max_length=10)
    address = models.TextField()
    admin_link = models.ForeignKey(TeacherProfile, on_delete=models.DO_NOTHING)
    is_verified = models.BooleanField(default=True)
    admin_name = models.CharField(max_length=20, blank=True)


class InstituteTeacher(models.Model):
    teacher_link = models.ForeignKey(TeacherProfile, on_delete=models.CASCADE)
    institute_link = models.ForeignKey(Institute, on_delete=models.CASCADE)
    administrative_right = models.BooleanField(default=False)


"""
class Class(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    teacher_link = models.ForeignKey(InstituteTeacher, on_delete=models.CASCADE, related_name='teacher_link')
    description = models.TextField(blank=True)


def renaming_uploaded_file1(instance, filename):
    return "institute/" + str(instance.class_link) + "/assignment/" + filename


def renaming_uploaded_file2(instance, filename):
    return "institute/" + str(instance.assignment_link.class_link) + "/assignment_submitted/" + filename


class Assignment(models.Model):
    class_link = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='code')
    given_datetime = models.DateField(auto_now_add=True)
    end_datetime = models.DateField()
    file = models.FileField(upload_to=renaming_uploaded_file1)
    description = models.CharField(max_length=256, blank=True)


class AssignmentSubmission(models.Model):
    assignment_link = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    submission_datetime = models.DateField(auto_now_add=True)
    time_remark = models.BooleanField(default=False)  # if on time then True
    ans_file = models.FileField(upload_to=renaming_uploaded_file2)
"""
