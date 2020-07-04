from django.db import models
from user_signup.models import TeacherProfile


class Subject(models.Model):
    subject_name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f'{self.subject_name}'


class StandardOrClass(models.Model):
    standard_or_class = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f'{self.standard_or_class}'


def renaming_uploaded_file1(instance, filename):
    return "video_material/" + str(instance.notes_link) + "/notes" + "_" + str(instance.pk) + "_" + filename


def renaming_uploaded_file2(instance, filename):
    return "video_material/" + str(instance.notes_link) + "/ques42323" + "_" + str(instance.pk) + "_" + filename


class VideoMaterial(models.Model):
    subject_link = models.ForeignKey(Subject, on_delete=models.CASCADE, to_field='subject_name')
    standard_link = models.ForeignKey(StandardOrClass, on_delete=models.CASCADE, to_field='standard_or_class')
    topic = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    video_link = models.URLField(blank=True)
    teacher_link = models.ForeignKey(TeacherProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'Topic: {self.topic}; Description: {self.description} '


class NotesMaterial(models.Model):
    notes_link = models.ForeignKey(VideoMaterial, on_delete=models.CASCADE,related_name='notes_material_link')
    notes = models.FileField(upload_to=renaming_uploaded_file1,blank=True)
    question_ans = models.FileField(upload_to=renaming_uploaded_file2, blank=True)

