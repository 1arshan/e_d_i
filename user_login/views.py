from rest_framework import generics
from .serializers import *
from subject_material.models import VideoMaterial
from rest_framework.response import Response
from django.contrib.auth.models import User
from user_signup.models import StudentProfile

class StudentHomePageView(generics.ListAPIView):
    serializer_class = StudentHomePageSerializer

    # c = request.user.StudentProfile
    def get_queryset(self):
        c = StudentProfile.objects.get(user=self.request.user).standard_or_class
        return VideoMaterial.objects.filter(standard_link=StudentProfile.objects.get
        (user=self.request.user).standard_or_class)
