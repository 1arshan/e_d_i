from django.shortcuts import render
from .models import Institute, InstituteTeacher
from .serializers import InstituteSerializer, InstituteTeacherSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from user_signup.models import TeacherProfile


# ----------get,post,put,patch of institute-------->>>>>>>>
# only admin has the right to update the institute
# to do open to view all teacher of institute
class InstituteView(generics.ListCreateAPIView, generics.UpdateAPIView):
    serializer_class = InstituteSerializer

    def get_queryset(self):
        username = self.request.user.username
        return Institute.objects.filter(admin_link=username)

    def create(self, request, *args, **kwargs):
        username = self.request.user.username
        serializer = self.serializer_class(data=self.request.data)
        if serializer.is_valid():
            serializer.validated_data['admin_link'] = TeacherProfile.objects.get(phone_number=username)
            serializer.save()
            x = {"msg": "institute save"}
            return Response(x, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        username = self.request.user.username
        try:
            t = Institute.objects.get(admin_link=username)
        except Exception:
            return Response("error", status=status.HTTP_400_BAD_REQUEST)
        serializer = self.serializer_class(t, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            x = {"msg": "institute info updated"}
            return Response(x, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InstituteTeacherView(generics.ListCreateAPIView, generics.UpdateAPIView):
    serializer_class = InstituteTeacherSerializer

    def get_queryset(self):
        username = self.request.user.username
        pk = Institute.objects.get(admin_link=username).pk
        return InstituteTeacher.objects.filter(institute_link=pk)
"""
class InstituteOtherView(generics.ListAPIView):
    serializer_class = InstituteSerializer
    
    def get_queryset(self):
        return Institute.objects.filter(pk=)"""