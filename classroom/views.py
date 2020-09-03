from django.shortcuts import render
from .models import Institute, InstituteTeacher, Class, Assignment, AssignmentSubmission,StudentAttach
from .serializers import InstituteSerializer, InstituteTeacherSerializer, ClassSerializer, \
    InstituteAssosiatedSerializer, AssingmentSerializer, AssingmentSubmissionSerializer, InstituteTeacherInfoSerializer \
    , ClassAdminSerializer, StudentAtatchSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from user_signup.models import TeacherProfile
from rest_framework.permissions import IsAuthenticated
import random
import string
from rest_framework.permissions import BasePermission


# ----------get,post,put,patch of institute-------->>>>>>>>
# ----------to Do remove admin_link

class InstituteView(generics.ListCreateAPIView, generics.UpdateAPIView,generics.DestroyAPIView):
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

    def delete(self, request, *args, **kwargs):
        username = self.request.user.username
        pk = self.request.GET['pk']
        try:
            t = Institute.objects.get(pk=pk, instituteteacher__teacher_link=username,
                                      instituteteacher__administrative_right=True)
            t.delete()
        except Exception:
            raise PermissionError


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
                raise PermissionError
                # return Response(x, status=status.HTTP_403_FORBIDDEN)
        except Exception:
            raise PermissionError
            # return Response(x, status=status.HTTP_403_FORBIDDEN)

    def get_queryset(self):
        institute_link = self.permission()
        # institute_link = self.request.GET['institute_link']
        return InstituteTeacher.objects.filter(institute_link=institute_link)

    def create(self, request, *args, **kwargs):
        data = self.request.data
        self.permission()
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            t = serializer.validated_data['teacher_link']
            if InstituteTeacher.objects.filter(teacher_link=t,
                                               institute_link=serializer.validated_data['institute_link']).exists():
                x = {"msg": "teacher already added"}
                return Response(x, status=status.HTTP_400_BAD_REQUEST)

            if self.request.GET['institute_link'] == data['institute_link']:
                serializer.save()
                x = {"msg": "teacher save"}
                return Response(x, status=status.HTTP_201_CREATED)
            raise PermissionError
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # ----to update techher profile---->>>>>>>
    def update(self, request, *args, **kwargs):
        pk = self.request.GET['pk']
        institute_link = self.permission()
        try:
            t = InstituteTeacher.objects.get(pk=pk, institute_link=institute_link)
        except Exception:
            return Response("error", status=status.HTTP_400_BAD_REQUEST)
        serializer = self.serializer_class(t, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            x = {"msg": "institute info updated"}
            return Response(x, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """def delete(self, request):
        institue_link = self.permission()
        pk = self.request.GET['pk']
        Institute.objects.get(pk=pk,in)
"""


def get_random_alphanumeric_string():
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(8)))
    return result_str


# -----CLasses------------------->>>>>>>
# institute_link is must
class ClassView(generics.ListCreateAPIView, generics.UpdateAPIView):
    serializer_class = ClassSerializer

    def permission(self):
        username = self.request.user.username
        x = {"msg": "you do not have permission"}
        institute_link = self.request.GET['institute_link']
        try:
            if InstituteTeacher.objects.get(institute_link=institute_link, teacher_link=username):
                return username
            else:
                raise PermissionError
                # return Response(x, status=status.HTTP_403_FORBIDDEN)
        except Exception:
            raise PermissionError
            # return Response(x, status=status.HTTP_403_FORBIDDEN)

    def get_queryset(self):
        user = self.request.user
        username = user.username
        institute_link = self.request.GET['institute_link']
        return Class.objects.filter(teacher_link=username, institute_link=institute_link)

    def create(self, request, *args, **kwargs):
        teacher_link = self.permission()
        result_str = "x"
        for i in range(15):
            result_str = get_random_alphanumeric_string()
            try:
                Class.objects.get(code=result_str)
                continue
            except Exception:
                break

        data = self.request.data
        data['code'] = result_str
        # data["teacher_link"] = teacher_link
        teacher_link = TeacherProfile.objects.get(phone_number=teacher_link)
        data["institute_link"] = self.request.GET['institute_link']
        serializer = self.serializer_class(data=self.request.data)
        if serializer.is_valid():
            serializer.validated_data["teacher_link"] = teacher_link
            serializer.save()
            x = {"msg": "class created"}
            return Response(x, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        pk = self.request.GET['pk']
        teacher_link = self.permission()
        try:
            t = Class.objects.get(pk=pk, teacher_link=teacher_link)
        except Exception:
            raise PermissionError
        serializer = self.serializer_class(t, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            x = {"msg": "class info updated"}
            return Response(x, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ---For admin to manage classes in his institute--->>>>>>
# ----institute link is must
class ClassAdminView(generics.ListCreateAPIView, generics.UpdateAPIView):
    serializer_class = ClassAdminSerializer

    def get_queryset(self):
        institute_link = InstituteTeacherView.permission(self)
        return Class.objects.filter(institute_link=institute_link)

    def create(self, request, *args, **kwargs):
        institute_link = InstituteTeacherView.permission(self)
        result_str = "x"
        for i in range(15):
            result_str = get_random_alphanumeric_string()
            try:
                Class.objects.get(code=result_str)
                continue
            except Exception:
                break
        data = self.request.data
        data['code'] = result_str
        data["institute_link"] = institute_link
        serializer = self.serializer_class(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            x = {"msg": "class created"}
            return Response(x, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        institute_link = InstituteTeacherView.permission(self)
        pk = self.request.GET['pk']
        try:
            t = Class.objects.get(pk=pk, institute_link=institute_link)
        except Exception:
            raise PermissionError
        serializer = self.serializer_class(t, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            x = {"msg": "class info updated"}
            return Response(x, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ----serializer validation and saving----->>>>
def serializer_validation_and_saving(self):
    serializer = self.serializer_class(data=self.request.data)
    if serializer.is_valid():
        serializer.save()
        return True
    return serializer.errors


"""
# ----serializer validation and updation----->>>>
def serializer_validation_and_update(self,request):
    serializer = self.serializer_class(t, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return 1
    return serializer.errors
"""


# ----For normal teacher---->>>>>
class Perm2(BasePermission):
    def has_permission(self, request, view):
        username = request.user.username
        class_link = request.GET['class_link']
        try:
            if Class.objects.get(pk=class_link, teacher_link=username):
                return True
            else:
                raise PermissionError
        except Exception:
            raise PermissionError


# ----class link is must ie.. PK of classs,---->>>>>
# ---for update pk is also required---------->>>>
class AssingmentView(generics.ListCreateAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    serializer_class = AssingmentSerializer
    permission_classes = [IsAuthenticated, Perm2]
    """def permission(self):
        username = self.request.user.username
        class_link = self.request.GET['class_link']
        try:
            if Class.objects.get(pk=class_link, teacher_link=username):
                return class_link
            else:
                raise PermissionError
        except Exception:
            raise PermissionError
"""

    def get_queryset(self):
        username = self.request.user.username
        class_link = self.request.GET['class_link']
        return Assignment.objects.filter(class_link=class_link, class_link__teacher_link=username)

    def create(self, request, *args, **kwargs):
        class_link = self.request.GET['class_link']
        data = request.data
        data['class_link'] = class_link
        x = {"msg": "Assinment Save"}
        response = serializer_validation_and_saving(self)
        if response == 1:
            return Response(x, status=status.HTTP_201_CREATED)
        else:
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        class_link = self.request.GET['class_link']
        pk = self.request.GET['pk']
        try:
            t = Assignment.objects.get(pk=pk, class_link=class_link)
        except Exception:
            raise PermissionError
        serializer = self.serializer_class(t, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            x = {"msg": "Assignment Updated"}
            return Response(x, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ----For admin teacher----------->>>>>>>>>>
# ---Permission ---->>>>
class Perm1(BasePermission):
    def has_permission(self, request, view):
        username = request.user.username
        class_link = request.GET['class_link']
        try:
            institute_link = Class.objects.get(pk=class_link).institute_link
            if InstituteTeacher.objects.get(teacher_link=username, institute_link=institute_link).administrative_right:
                return True
            else:
                raise PermissionError
        except Exception:
            raise PermissionError


# -----class_link is must ie PK of classes------>>>>>>
# ------for update pk is also required-------->>>>>>
class AssingmentAdminView(generics.ListCreateAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    serializer_class = AssingmentSerializer
    permission_classes = [IsAuthenticated, Perm1]

    def get_queryset(self):
        class_link = self.request.GET['class_link']
        return Assignment.objects.filter(class_link=class_link)

    def create(self, request, *args, **kwargs):
        response = AssingmentView.create(self, request, *args, **kwargs)
        return response

    def update(self, request, *args, **kwargs):
        response = AssingmentView.update(self, request, *args, **kwargs)
        return response


# -----just for info for teacher to know to which all institute they are assosiated with-->>>
class InstituteTeacherAssosiatedView(generics.ListAPIView):
    serializer_class = InstituteAssosiatedSerializer

    def get_queryset(self):
        username = self.request.user.username
        t = InstituteTeacher.objects.filter(teacher_link=username).values('institute_link', 'administrative_right')
        y = []
        z = []
        for x in t:
            y.append(x['institute_link'])
            if x['administrative_right']:
                z.append(x['institute_link'])
        u = Institute.objects.filter(pk__in=y).values()
        for w in u:
            if w['id'] in z:
                w['administrative_right'] = True
            else:
                w['administrative_right'] = False
        return u


# ---for anyone to see institute detail
class InstituteOtherView(generics.ListAPIView):
    serializer_class = InstituteSerializer

    def get_queryset(self):
        return Institute.objects.filter(pk=self.request.GET['pk'])


#  To DO ---teacer see all teacher assosiated with institurte


# ------For  Teacher----->>>>
class Perm4(BasePermission):
    def has_permission(self, request, view):
        username = request.user.username
        class_link = request.GET['class_link']
        try:
            if Class.objects.get(pk=class_link, teacher_link=username):
                return True
            else:
                raise PermissionError
        except Exception:
            raise PermissionError


# ------Teacher to see assign submitted----->>>>
class AssingmentSubmittedView(generics.ListAPIView):
    serializer_class = AssingmentSubmissionSerializer
    permission_classes = [IsAuthenticated, Perm4]

    def get_queryset(self):
        assingmnet_link = self.request.GET['assingmnet_link']
        class_link = self.request.GET['class_link']
        return AssignmentSubmission.objects.filter(assignment_link=assingmnet_link)


# ----For admin----->>>
# ---admin to see assignment submitted ----->>>>>
# ---class_link,ass_link
class AssingmentAdminSubmittedView(generics.ListAPIView):
    serializer_class = AssingmentSubmissionSerializer
    permission_classes = [IsAuthenticated, Perm1]

    def get_queryset(self):
        assingmnet_link = self.request.GET['assingmnet_link']
        return AssignmentSubmission.objects.filter(assignment_link=assingmnet_link)


# ----For non admin
# ----need institute_link------>>>>
class InstituteTeacherInfoView(generics.ListAPIView):
    serializer_class = InstituteTeacherInfoSerializer

    def get_queryset(self):
        institute_link = self.request.GET['institute_link']
        username = self.request.user.username
        try:
            InstituteTeacher.objects.get(institute_link=institute_link, teacher_link=username)
            return InstituteTeacher.objects.filter(institute_link=institute_link)
        except Exception:
            raise PermissionError


# ---For teacher------->>>>
# ---to see student in the class
class TeacherStudentView(generics.ListAPIView):
    serializer_class = StudentAtatchSerializer

    def get_queryset(self):
        class_link = self.request.GET['class_link']
        return StudentAttach.objects.filter(class_link=class_link,class_link__teacher_link=self.request.user.username)
