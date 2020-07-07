from rest_framework import generics
from .serializers import *
from subject_material.models import VideoMaterial
from user_signup.models import StudentProfile
from rest_framework.permissions import IsAuthenticated


class StudentHomePageView(generics.ListAPIView):
    serializer_class = StudentHomePageSerializer
    permission_classes = [IsAuthenticated]
    # c = request.user.StudentProfile
    def get_queryset(self):
        #c = StudentProfile.objects.get(user=self.request.user).standard_or_class
        return VideoMaterial.objects.filter(standard_link=StudentProfile.objects.get
        (user=self.request.user).standard_or_class)
