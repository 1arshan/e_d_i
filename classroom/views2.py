from django.shortcuts import render
from .models import Institute, InstituteTeacher, Class, Assignment, StudentAttach
from .serializers import InstituteSerializer, InstituteTeacherSerializer, ClassSerializer, \
    InstituteAssosiatedSerializer, AssingmentSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
import random
import string
from rest_framework.permissions import BasePermission
from user_signup.models import StudentProfile,TeacherProfile


# ---For studnet to see all classes in which they are log in
# ----For get: class link(pk) send; for post class code send
class StudentClassView(generics.ListCreateAPIView):
    serializer_class = ClassSerializer

    def get_queryset(self):
        username = self.request.user.username
        t = StudentAttach.objects.filter(student_link=username).values('class_link')
        l = []
        for x in t:
            l.append(x['class_link'])
        return Class.objects.filter(pk__in=l)

    def create(self, request, *args, **kwargs):
        data = request.data
        username = self.request.user.username

        try:
            data = Class.objects.get(code=data['code'])
            try:
                StudentAttach.objects.get(class_link=data.pk, student_link=username)
                x = {"msg": "already added to that class"}
                return Response(x, status=status.HTTP_400_BAD_REQUEST)
            except Exception:
                student_data = StudentProfile.objects.get(phone_number=username)
                StudentAttach.objects.create(class_link=data, student_link=student_data)
                x = {"msg": "added to class"}
                return Response(x, status=status.HTTP_201_CREATED)
        except Exception:
            x = {"msg": "class code wrong"}
            return Response(x, status=status.HTTP_400_BAD_REQUEST)

class StudentAssignmentView(generics.ListCreateAPIView,generics.UpdateAPIView,generics.DestroyAPIView):
    pass