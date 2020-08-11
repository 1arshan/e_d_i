from django.shortcuts import render
from .models import Institute, InstituteTeacher, Class
from .serializers import InstituteSerializer, InstituteTeacherSerializer, ClassSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from user_signup.models import TeacherProfile


# ----------get,post,put,patch of institute-------->>>>>>>>
# ----------to Do remove admin_link

class InstituteView(generics.ListCreateAPIView, generics.UpdateAPIView):
    serializer_class = InstituteSerializer

    def get_queryset(self):
        username = self.request.user.username
        t = InstituteTeacher.objects.filter(teacher_link=username,
                                            administrative_right=True).values('institute_link')
        y = []
        for x in t:
            y.append(x['institute_link'])
        return Institute.objects.filter(pk__in=y)

    def create(self, request, *args, **kwargs):
        username = self.request.user.username
        serializer = self.serializer_class(data=self.request.data)
        if serializer.is_valid():
            teacher_data = TeacherProfile.objects.get(phone_number=username)
            # serializer.validated_data['admin_link'] = teacher_data
            data = serializer.save()
            x = {"msg": "institute save"}
            InstituteTeacher.objects.create(teacher_link=teacher_data, administrative_right=True, institute_link=data)
            return Response(x, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        username = self.request.user.username
        pk = self.request.GET['pk']
        try:
            t = Institute.objects.get(pk=pk, instituteteacher__teacher_link=username,
                                      instituteteacher__administrative_right=True)
        except Exception:
            return Response("error", status=status.HTTP_400_BAD_REQUEST)
        serializer = self.serializer_class(t, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            x = {"msg": "institute info updated"}
            return Response(x, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# -- managing teacher of a institute for admin or who have administrative right
# -----get ,post,update----->>>>
class InstituteTeacherView(generics.ListCreateAPIView, generics.UpdateAPIView):
    serializer_class = InstituteTeacherSerializer

    def permission(self):
        username = self.request.user.username
        x = {"msg": "you do not have permission to view this content"}
        institute_link = self.request.GET['institute_link']
        try:
            if InstituteTeacher.objects.get(institute_link=institute_link, teacher_link=username).administrative_right:
                return institute_link
            else:
                return Response(x, status=status.HTTP_403_FORBIDDEN)
        except Exception:
            return Response(x, status=status.HTTP_403_FORBIDDEN)

    def get_queryset(self):
        institute_link = self.permission()
        institute_link = self.request.GET['institute_link']
        return InstituteTeacher.objects.filter(institute_link=institute_link)

    def create(self, request, *args, **kwargs):
        self.permission()
        serializer = self.serializer_class(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            x = {"msg": "teacher save"}
            return Response(x, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # ----to update techher profile---->>>>>>>
    def update(self, request, *args, **kwargs):
        pk = self.request.GET['pk']
        self.permission()
        try:
            t = InstituteTeacher.objects.get(pk=pk)
        except Exception:
            return Response("error", status=status.HTTP_400_BAD_REQUEST)
        serializer = self.serializer_class(t, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            x = {"msg": "institute info updated"}
            return Response(x, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ------class

class ClassView(generics.ListCreateAPIView, generics.UpdateAPIView):
    serializer_class = ClassSerializer

    def get_queryset(self):
        username = self.request.user.username
        institute_link = self.request.GET['institute_link']
        return Class.objects.filter(teacher_link=username, institute_link=institute_link)


# -----just for info for teacher to know to which all institute they are assosiated with-->>>
class InstituteTeacherAssosiatedView(generics.ListAPIView):
    serializer_class = InstituteSerializer

    def get_queryset(self):
        username = self.request.user.username
        t = InstituteTeacher.objects.filter(teacher_link=username).values('institute_link')
        y = []
        for x in t:
            y.append(x['institute_link'])
        return Institute.objects.filter(pk__in=y)


# ---for anyone to see institute detail
class InstituteOtherView(generics.ListAPIView):
    serializer_class = InstituteSerializer

    def get_queryset(self):
        return Institute.objects.filter(pk=self.request.GET['pk'])
