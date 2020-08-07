from django.db import models
from user_signup.models import TeacherProfile
from subject_material.models import VideoMaterial


class TeacherVerification(TeacherProfile):
    class Meta:
        proxy = True


class VideoMaterialVerification(VideoMaterial):
    class Meta:
        proxy = True


class CrashReport(models.Model):
    app_version_code = models.CharField(max_length=50)
    app_version_name = models.CharField(max_length=50)
    andriod_version = models.CharField(max_length=50)
    package_name = models.CharField(max_length=50)
    build = models.CharField(max_length=50)
    stack_trace = models.TextField()

