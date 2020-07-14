from django.db import models
from user_signup.models import TeacherProfile
from subject_material.models import VideoMaterial


class TeacherVerification(TeacherProfile):
    class Meta:
        proxy = True


class VideoMaterialVerification(VideoMaterial):
    class Meta:
        proxy = True
