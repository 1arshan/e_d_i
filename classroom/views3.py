"""from .models import QuestionBank, StudentTest, ClassTest, Class,StudentAttach
from .serializers import QuestionBankSerializer, StudentResultGetSerializer, ClassTestSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import BasePermission
from user_signup.models import StudentProfile, TeacherProfile
from datetime import datetime, timezone


# ---For teacher
class Perm1(BasePermission):
    def has_permission(self, request, view):
        username = request.user.username
        # assignment_link = request.GET['assignment_link']
        try:
            TeacherProfile.objects.get(phone_number=username)
            return True
        except Exception:
            raise PermissionError


# ---class_link,subject_link,chapter,-----

class QuestionBankView(generics.ListCreateAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    serializer_class = QuestionBankSerializer
    permission_classes = [IsAuthenticated, Perm1]

    def get_queryset(self):
        class_link = self.request.GET['class_link']
        try:
            subject_link = self.request.GET['subject_link']
            try:
                chapter = self.request.GET['chapter']
                return QuestionBank.objects.filter(chapter=chapter, subject_link=subject_link, class_link=class_link,
                                                   public_access=True)
            except Exception:
                return QuestionBank.objects.filter(subject_link=subject_link, class_link=class_link, public_access=True)
        except Exception:
            return QuestionBank.objects.filter(class_link=class_link, public_access=True)

    def create(self, request, *args, **kwargs):
        data = self.request.data
        data['created_by'] = self.request.user.pk
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()

            x = {"msg": "Question Added"}
            return Response(x, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        pk = self.request.GET['pk']
        t = QuestionBank.objects.get(pk=pk)
        serializer = self.serializer_class(t, data=request.data, partial=True)
        if serializer.is_valid():
            if t.created_by == self.request.user:
                serializer.save()
            else:
                raise PermissionError
            x = {"msg": "Question Bank  updated"}
            return Response(x, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        pk = self.request.GET['pk']
        t = QuestionBank.objects.get(id=pk)
        if t.created_by == self.request.user:
            t.delete()
        else:
            raise PermissionError
        x = {"msg": "Question Deleted"}
        return Response(x, status=status.HTTP_201_CREATED)


class QuestionBankPrivateView(generics.ListAPIView):
    serializer_class = QuestionBankSerializer

    def get_queryset(self):
        username = self.request.user.pk
        class_link = self.request.GET['class_link']
        try:
            subject_link = self.request.GET['subject_link']
            try:
                chapter = self.request.GET['chapter']
                return QuestionBank.objects.filter(chapter=chapter, subject_link=subject_link, class_link=class_link
                                                   , created_by=username)
            except Exception:
                return QuestionBank.objects.filter(subject_link=subject_link, class_link=class_link,
                                                   created_by=username)
        except Exception:
            return QuestionBank.objects.filter(class_link=class_link, created_by=username)


# ---For student--->>>>
# ---noq---is nessesary--->
class MockTestView(generics.ListAPIView):
    serializer_class = QuestionBankSerializer

    def get_queryset(self):
        noq = self.request.GET['noq']
        noq = int(noq)
        class_link = self.request.GET['class_link']
        try:
            subject_link = self.request.GET['subject_link']
            try:
                chapter = self.request.GET['chapter']
                return QuestionBank.objects.filter(chapter=chapter, subject_link=subject_link, class_link=class_link)[
                       :noq]
            except Exception:
                return QuestionBank.objects.filter(subject_link=subject_link, class_link=class_link)[:noq]
        except Exception:
            return QuestionBank.objects.filter(class_link=class_link)[:noq]


# ---For student to see their result
class MockTestResultGetView(generics.ListCreateAPIView):
    serializer_class = StudentResultGetSerializer

    def get_queryset(self):
        return StudentTest.objects.filter(student_link=self.request.user.pk)

    def create(self, request, *args, **kwargs):
        data = self.request.data
        data['student_link'] = self.request.user.pk
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            x = {"msg": "Result Save"}
            return Response(x, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ---For teacehr----->>>
class Perm2(BasePermission):
    def has_permission(self, request, view):
        username = request.user.username
        class_link = request.GET['class_link']
        try:
            Class.objects.get(pk=class_link, teacher_link=username)
            return True
        except Exception:
            raise PermissionError


# to create clss test--->>>
class ClassTestTeacherView(generics.ListCreateAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    serializer_class = ClassTestSerializer
    permission_classes = [IsAuthenticated, Perm2]

    def get_queryset(self):
        class_link = self.request.GET['class_link']
        return ClassTest.objects.filter(class_link=class_link)

    def create(self, request, *args, **kwargs):
        data = self.request.data
        data['class_link'] = self.request.GET['class_link']
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            x = {"msg": "Test Created"}
            return Response(x, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        pk = self.request.GET['pk']
        class_link = self.request.GET['class_link']
        t = ClassTest.objects.get(id=pk,class_link=class_link)
        t.delete()
        x = {"msg": "Test Deleted"}
        return Response(x, status=status.HTTP_201_CREATED)



#For student to give their test--->>>
class Perm3(BasePermission):
    def has_permission(self, request, view):
        username = request.user.username
        class_link = request.GET['class_link']
        try:
            StudentAttach.objects.get(class_link=class_link, student_link=username)
            return True
        except Exception:
            raise PermissionError


class ClassTestStudentView(generics.ListAPIView):
    serializer_class = ClassTestSerializer
    permission_classes = [IsAuthenticated, Perm3]

    def get_queryset(self):
        class_link = self.request.GET['class_link']
        t = ClassTest.objects.filter(class_link=class_link).values()
        print(t)
        return ClassTest.objects.filter(class_link=class_link)
"""