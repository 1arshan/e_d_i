from django.db import models
from user_signup.models import TeacherProfile
from django_better_admin_arrayfield.models.fields import ArrayField


class Subject(models.Model):
    subject_name = models.CharField(max_length=20, unique=True)
    field_name = ArrayField(models.CharField(max_length=20, blank=True), blank=True)

    def __str__(self):
        return f'{self.subject_name}'


class StandardOrClass(models.Model):
    standard_or_class = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f'{self.standard_or_class}'


def renaming_uploaded_file1(instance, filename):
    material = instance.notes_link

    route = str(
        material.standard_link.standard_or_class + "/" + material.subject_link.subject_name + "/" + material.chapter + "/" + material.topic)
    return "video_material/" + route + "/notes" + "_" + filename


# str(instance.notes_link) +
def renaming_uploaded_file2(instance, filename):
    material = instance.notes_link
    route = str(
        material.standard_link.standard_or_class + "/" + material.subject_link.subject_name + "/" + material.chapter + "/" + material.topic)
    return "video_material/" + route + "/ques" + "_" + filename


def renaming_uploaded_file3(instance, filename):
    route = str(
        instance.standard_link.standard_or_class+"/"+instance.subject_link.subject_name+"/"+instance.chapter+"/"+instance.topic)
    return "video_material/" + route + "/thumbnail" + "_" + filename


class VideoMaterial(models.Model):
    thumbnail = models.ImageField(blank=True, upload_to=renaming_uploaded_file3)
    subject_link = models.ForeignKey(Subject, on_delete=models.CASCADE, to_field='subject_name')
    standard_link = models.ForeignKey(StandardOrClass, on_delete=models.CASCADE, to_field='standard_or_class')
    chapter = models.CharField(max_length=30)
    topic = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    video_link = models.URLField(blank=True)
    teacher_link = models.ForeignKey(TeacherProfile, on_delete=models.CASCADE, to_field='phone_number')
    teacher_name = models.CharField(max_length=50, default='Anonymous')
    is_verified = models.BooleanField(default=True)
    date_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Topic: {self.topic}; Subject: {self.subject_link}; Class: {self.standard_link} '


class NotesMaterial(models.Model):
    notes_link = models.ForeignKey(VideoMaterial, on_delete=models.CASCADE, related_name='notes_material_link')
    notes = models.FileField(upload_to=renaming_uploaded_file1, blank=True)
    question_ans = models.FileField(upload_to=renaming_uploaded_file2, blank=True)
