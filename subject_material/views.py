from user_login.serializers import StudentHomePageSerializer
from rest_framework import generics
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import VideoMaterial

class StudyMaterialUploadView(generics.ListCreateAPIView):
    serializer_class = StudentHomePageSerializer

    def get_queryset(self):
        user =self.request.user.username
        return VideoMaterial.objects.filter(teacher_link=user)


