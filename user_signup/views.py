from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import TempStudent, StudentProfile, TempTeacher, TeacherProfile, TestingModel
from .serializers import TempStudentSerializer, TempTeacherSerializer, StudentSerializer, TeacherSerializer, \
    TestingModelSerializer
from datetime import datetime, timezone
from django.contrib.auth.models import User
from broadcaster.mail import MailVerification
from django.core import exceptions
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from adcbackend.token import get_tokens_for_user, account_activation_token
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode
from django.http import HttpResponse
from django.contrib.auth.models import Group
from subject_material.models import VideoMaterial
from .tasks import send_parallel_sms, send_parallel_mail
import random
import base64


# temperory student model till phone number verified
class TempStudentView(APIView):
    permission_classes = []

    def post(self, request):
        data = request.data
        try:
            t = TempStudent.objects.get(phone_number=data['phone_number'])
            serializer = TempStudentSerializer(t, data=data)

        except Exception:
            serializer = TempStudentSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            x = {"msg": "otp sent"}
            return Response(x, status=status.HTTP_201_CREATED)
        x = {"msg": "something went wrong please retry"}
        return Response(x, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, ph_no):
        try:
            data = TempStudent.objects.get(phone_number=ph_no)
        except exceptions.ObjectDoesNotExist:
            y = {"msg": "This phone number does not exist"}
            return Response(y, status=status.HTTP_400_BAD_REQUEST)
        diff = datetime.now(timezone.utc) - data.date
        if diff.seconds > 20:
            data.otp = "1234"  # just a type of signal
            data.save()
            x = {"msg": "resend"}
            return Response(x, status=status.HTTP_202_ACCEPTED)
        else:
            x = {"msg": "wait"}
            return Response(x, status=status.HTTP_200_OK)


# do tranfering data and deleting in parallelism
# otp verify and tranfers user data,email verification if provided
class StudentVerifyOtpView(APIView):
    permission_classes = []

    def post(self, request):
        data_receive = request.data
        data = TempStudent.objects.get(phone_number=data_receive['phone_number'])
        diff = datetime.now(timezone.utc) - data.date
        if diff.seconds < 5000:
            if data_receive["otp"] == data.otp:
                try:
                    user = User.objects.get(username=str(int(data.phone_number) * 30))
                    user.username = data.phone_number
                    user.save()

                except Exception as e:
                    y = {"msg": "user with this phone number already exist"}
                    return Response(y, status=status.HTTP_406_NOT_ACCEPTABLE)
                try:

                    StudentProfile.objects.create(standard_or_class=data.standard_or_class, user=user,
                                                  pincode=data.pincode, phone_number=data.phone_number,
                                                  email=data.email, last_name=data.last_name
                                                  , first_name=data.first_name, course_field=data.course_field)
                except Exception as e:
                    user.delete()
                    y = {"msg": "phone number enter already exist"}
                    return Response(y, status=status.HTTP_406_NOT_ACCEPTABLE)
                data.delete()
                if user.email:
                    MailVerification(user, type='s')
                    mail_otp = "please verify your mail also"
                else:
                    mail_otp = "it will be better if you also provide us your email address"

                x = get_tokens_for_user(user)
                x["msg"] = "otp verififed, Account actiuated"
                x['mail'] = mail_otp
                return Response(x, status=status.HTTP_202_ACCEPTED)
            y = {"msg": 'otp incorrect'}
            return Response(y, status=status.HTTP_200_OK)
        y = {"msg": "otp expire"}
        return Response(y, status=status.HTTP_200_OK)


# temperory teacher model till phone number verified
class TempTeacherView(APIView):
    permission_classes = []

    def post(self, request):
        data = request.data
        try:
            t = TempTeacher.objects.get(phone_number=data['phone_number'])
            serializer = TempTeacherSerializer(t, data=data)

        except Exception:
            serializer = TempTeacherSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            x = {"msg": "otp sent"}
            return Response(x, status=status.HTTP_201_CREATED)
        x = {"msg": "something went wrong please retry"}
        return Response(x, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, ph_no):
        try:
            data = TempTeacher.objects.get(phone_number=ph_no)
        except exceptions.ObjectDoesNotExist:
            x = {"msg": "This phone number does not exist"}
            return Response(x, status=status.HTTP_400_BAD_REQUEST)
        diff = datetime.now(timezone.utc) - data.date
        if diff.seconds > 20:
            data.otp = "1234"  # just a type of signal
            data.save()
            x = {"msg": "resend"}
            return Response(x, status=status.HTTP_202_ACCEPTED)
        else:
            x = {"msg": "wait"}
            return Response(x, status=status.HTTP_200_OK)


# do tranfering data and deleting in parallelism
# otp verify and tranfers user data,email verification if provided
class TeacherVerifyOtpView(APIView):
    permission_classes = []

    def post(self, request):
        data_receive = request.data
        data = TempTeacher.objects.get(phone_number=data_receive['phone_number'])
        diff = datetime.now(timezone.utc) - data.date
        if diff.seconds < 500:
            if data_receive["otp"] == data.otp:
                try:
                    user = User.objects.get(username=str(int(data.phone_number) * 30))
                    user.username = data.phone_number
                    user.save()

                except Exception as e:
                    x = {"msg": "user with this phone number already exist"}
                    return Response(x, status=status.HTTP_406_NOT_ACCEPTABLE)

                try:
                    TeacherProfile.objects.create(teacher_description=data.description, user=user
                                                  , phone_number=data.phone_number,
                                                  email=data.email, last_name=data.last_name,
                                                  first_name=data.first_name, subject=data.subject,
                                                  experience=data.experience, max_qualification=data.max_qualification)

                except Exception as e:
                    user.delete()
                    x = {"msg": "user with this email already exist"}
                    return Response(x, status=status.HTTP_406_NOT_ACCEPTABLE)

                data.delete()

                if user.email:
                    MailVerification(user, type='t')
                    mail_otp = "please verify your mail also"
                else:
                    mail_otp = "it will be better if you also provide us your email address"

                my_group = Group.objects.get(name='Teacher')
                my_group.user_set.add(user)
                user.is_staff = True
                user.save()

                x = get_tokens_for_user(user)
                x["msg"] = "otp verififed, Account actiuated"
                x['mail'] = mail_otp
                return Response(x, status=status.HTTP_202_ACCEPTED)
            x = {"msg": "OTP incorrect"}
            return Response(x, status=status.HTTP_200_OK)
        x = {"msg": "OTP expire"}
        return Response(x, status=status.HTTP_200_OK)


# --student profile view and change,user model has not change-->>>
class StudetProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = StudentSerializer(StudentProfile.objects.get(phone_number=self.request.user.username))
        return Response(serializer.data)

    def put(self, request):
        user = self.request.user.username
        t = StudentProfile.objects.get(phone_number=user)
        serializer = StudentSerializer(t, data=request.data)
        if serializer.is_valid():
            u = User.objects.get(username=user)
            u.first_name = serializer.validated_data['first_name']
            u.last_name = serializer.validated_data['last_name']
            serializer.save()
            u.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# --techer profile view and change,user model has not change-->>>
class TeacherProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = TeacherSerializer(TeacherProfile.objects.get(phone_number=self.request.user.username))
        return Response(serializer.data)

    def put(self, request):
        user = self.request.user.username
        t = TeacherProfile.objects.get(phone_number=user)
        serializer = TeacherSerializer(t, data=request.data)
        if serializer.is_valid():
            serializer.save()
            u = User.objects.get(username=user)
            u.first_name = serializer.validated_data['first_name']
            u.last_name = serializer.validated_data['last_name']
            u.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# do a redirection to login page
# email verififcation
def activate_account(request, uidb64, token, typ):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        return HttpResponse('Activation link is invalid!', status=status.HTTP_200_OK)
    if user is not None and account_activation_token.check_token(user, token):
        if typ == 't':
            user.teacherprofile.email_verified = True
            user.teacherprofile.save()
        elif typ == 's':
            user.studentprofile.email_verified = True
            user.studentprofile.save()
        return HttpResponse('Email_verified', status=status.HTTP_201_CREATED)
    else:
        return HttpResponse('Activation link is invalid!', status=status.HTTP_200_OK)

"""
class TestingView(generics.ListCreateAPIView):
    permission_classes = []
    serializer_class = TestingModelSerializer

    # queryset = VideoMaterial.objects.all()

    def get_queryset(self):
        data = self.request.data
        return VideoMaterial.objects.filter(standard_link=data['standard_link'],
                                            subject_link=data['subject_link'],
                                            chapter=data['chapter'])

    def create(self, request, *args, **kwargs):
        data = self.request.data
        print(data)
        return Response("dsds")
"""

class TestingView(APIView):
    permission_classes = []

    def post(self, request):
        data = self.request.data
        x =VideoMaterial.objects.filter(standard_link=data['standard_link'],subject_link=data['subject_link'],
                                        chapter=data['chapter'])
        serializer = TestingModelSerializer(x,many=True)
        return Response(serializer.data)

