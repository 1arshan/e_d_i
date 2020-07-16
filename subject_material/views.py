from .serializers import TeacherUploadSerializer
from rest_framework import generics
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import VideoMaterial
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from user_signup.models import TeacherProfile
from django.contrib.auth.models import User


class StudyMaterialUploadView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = self.request.user.username
        serializer = TeacherUploadSerializer(VideoMaterial.objects.filter(teacher_link=user), many=True)
        return Response(serializer.data)

    def post(self, request):
        user = self.request.user
        teacher_name = TeacherProfile.objects.get(user=user)
        serializer = TeacherUploadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['teacher_link'] = teacher_name
            serializer.save()
            return Response("save", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


