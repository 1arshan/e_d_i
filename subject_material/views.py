from .serializers import TeacherUploadSerializerGet, TeacherUploadSerializerPost
from user_login.serializers import NotesMaterialSerializer
from rest_framework import generics
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import VideoMaterial
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from user_signup.models import TeacherProfile


# -----give subject,class,chapter get back all video material intersection-----
class TeacherChapterView(APIView):

    def get(self, request):
        serializer = TeacherUploadSerializerGet(VideoMaterial.objects.filter(standard_link=self.request.GET['class'],
                                                                             subject_link=self.request.GET['subject'],
                                                                             chapter__iexact=request.GET['chapter'],
                                                                             teacher_link=self.request.user.username,
                                                                             is_verified=True), many=True)
        return Response(serializer.data)

    def post(self, request):
        user = self.request.user
        teacher_name = TeacherProfile.objects.get(user=user)
        serializer = TeacherUploadSerializerPost(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['teacher_link'] = teacher_name
            serializer.save()
            x = {"id": serializer.data['id']}
            return Response(x, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TeacherChapterNotesView(APIView):

    def post(self, request):
        serializer = NotesMaterialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            x = {"msg": "material save"}
            return Response(x, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
