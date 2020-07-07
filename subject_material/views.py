from user_login.serializers import StudentHomePageSerializer
from rest_framework import generics
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import VideoMaterial
from rest_framework.permissions import IsAuthenticated

class StudyMaterialUploadView(generics.ListCreateAPIView):
    #permission_classes = [IsAuthenticated]
    serializer_class = StudentHomePageSerializer

    def get_queryset(self):
        user = self.request.user.username
        print(user)
        return VideoMaterial.objects.filter(teacher_link=user)
        #return VideoMaterial.objects.all()