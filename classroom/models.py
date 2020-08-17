from django.db import models
from user_signup.models import TeacherProfile, StudentProfile


class Institute(models.Model):
    name = models.CharField(max_length=60)
    pincode = models.CharField(max_length=10)
    address = models.TextField()
    is_verified = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name)


class InstituteTeacher(models.Model):
    teacher_link = models.ForeignKey(TeacherProfile, on_delete=models.CASCADE)
    institute_link = models.ForeignKey(Institute, on_delete=models.CASCADE)
    administrative_right = models.BooleanField(default=False)

    def __str__(self):
        return f'Teacher: {self.teacher_link}; Institute: {self.institute_link}'


class Class(models.Model):
    code = models.CharField(max_length=10, unique=True)
    standard_or_class = models.CharField(max_length=10, default="null")
    # = models.CharField(max_length=30)
    teacher_link = models.ForeignKey(TeacherProfile, on_delete=models.DO_NOTHING)
    institute_link = models.ForeignKey(Institute, on_delete=models.CASCADE)
    description = models.CharField(max_length=256, blank=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.code}'


def renaming_uploaded_file1(instance, filename):
    return "institute/" + str(instance.class_link) + "/assignment/" + filename


def renaming_uploaded_file2(instance, filename):
    return "institute/" + str(instance.assignment_link.class_link) + "/assignment_submitted/" + filename


class Assignment(models.Model):
    class_link = models.ForeignKey(Class, on_delete=models.CASCADE,to_field='id')
    given_datetime = models.DateTimeField(auto_now_add=True)
    end_datetime = models.DateTimeField()
    file = models.FileField(upload_to=renaming_uploaded_file1)
    description = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return f'Assignmnet link:{str(self.pk)} ; class link:{self.class_link}'


class StudentAttach(models.Model):
    class_link = models.ForeignKey(Class, on_delete=models.CASCADE,to_field='id')
    student_link = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.class_link)


class AssignmentSubmission(models.Model):
    assignment_link = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    submission_datetime = models.DateTimeField(auto_now_add=True)
    time_remark = models.BooleanField(default=False)  # if on time then True
    ans_file = models.FileField(upload_to=renaming_uploaded_file2)
    student_link=models.ForeignKey(StudentProfile,on_delete=models.DO_NOTHING)
