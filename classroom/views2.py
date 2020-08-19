from django.shortcuts import render
from .models import Institute, InstituteTeacher, Class, Assignment, StudentAttach, AssignmentSubmission
from .serializers import InstituteSerializer, InstituteTeacherSerializer, ClassSerializer, \
    InstituteAssosiatedSerializer, AssingmentSerializer, AssingmentSubmissionSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
import random
import string
from rest_framework.permissions import BasePermission
from user_signup.models import StudentProfile, TeacherProfile
from datetime import datetime, timezone


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


# ---For studetn---->>>>
# ----class link is must  will be pass in url------>>>>>>>
class StudentAssignmentView(generics.ListAPIView):
    serializer_class = AssingmentSerializer

    def get_queryset(self):
        class_link = self.request.GET['class_link']
        return Assignment.objects.filter(class_link=class_link)


# ---For studetn---->>>>
class Perm1(BasePermission):
    def has_permission(self, request, view):
        username = request.user.username
        #assignment_link = request.GET['assignment_link']
        try:

            class_link = request.GET['class_link']
            StudentAttach.objects.get(class_link_id=class_link, student_link=username)
            return True
        except Exception:
            raise PermissionError


# ----assignmetn link is must------>>>>>>>
class StudentAssignmentSubmissionView(generics.ListCreateAPIView, generics.UpdateAPIView):
    serializer_class = AssingmentSubmissionSerializer
    permission_classes = [IsAuthenticated, Perm1]

    def get_queryset(self):
        username = self.request.user.username
        assingmnet_link = self.request.GET['assignment_link']
        return AssignmentSubmission.objects.filter(assignment_link=assingmnet_link, student_link=username)

    def create(self, request, *args, **kwargs):
        data = self.request.data
        date = datetime.now(timezone.utc)
        assingmnet_link = self.request.GET['assignment_link']
        end_datetime = Assignment.objects.get(pk=assingmnet_link).end_datetime
        if end_datetime > date:
            data['time_remark'] = True
        data['student_link'] = self.request.user.username
        data['assignment_link'] = assingmnet_link
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            x = {"msg": "Assignmnet Submitted"}
            return Response(x, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        pk = self.request.GET['pk']
        t = AssignmentSubmission.objects.get(pk=pk, student_link=self.request.user.username)
        serializer = self.serializer_class(t, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            x = {"msg": "Assignment Submitted updated"}
            return Response(x, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
