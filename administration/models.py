from django.db import models
from user_signup.models import TeacherProfile


class TeacherVerification(TeacherProfile):
    class Meta:
        proxy = True
