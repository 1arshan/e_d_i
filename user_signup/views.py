from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import TempStudent, StudentProfile, TempTeacher, TeacherProfile
from .serializers import TempStudentSerializer, TempTeacherSerializer
from datetime import datetime, timezone
from django.core import exceptions
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from broadcaster.mail import MailVerification
from django.contrib.auth import login


# temperory student model till phone number verified
class TempStudentView(APIView):

    def post(self, request):
        data = request.data
        try:
            t = TempStudent.objects.get(phone_number=data['phone_number'])
            serializer = TempStudentSerializer(t, data=data)

        except Exception:
            serializer = TempStudentSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response("otp sent", status=status.HTTP_201_CREATED)
        return Response("something went wrong please retry", status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, ph_no):
        try:
            data = TempStudent.objects.get(phone_number=ph_no)
        except exceptions.ObjectDoesNotExist:
            return Response("This phone number does not exist", status=status.HTTP_400_BAD_REQUEST)
        diff = datetime.now(timezone.utc) - data.date
        if diff.seconds > 20:
            data.otp = "1234"  # just a type of signal
            data.save()
            return Response("resend", status=status.HTTP_202_ACCEPTED)
        else:
            return Response("wait", status=status.HTTP_200_OK)


# do tranfering data and deleting in parallelism
# otp verify and tranfers user data,email verification if provided
class StudentVerifyOtpView(APIView):
    def post(self, request):
        data_receive = request.data
        data = TempStudent.objects.get(phone_number=data_receive['phone_number'])
        diff = datetime.now(timezone.utc) - data.date
        if diff.seconds < 500:
            if data_receive["otp"] == data.otp:
                try:
                    user = User.objects.create_user(username=data.phone_number, email=data.email,
                                                    password=data.password, first_name=data.first_name,
                                                    last_name=data.last_name)
                except Exception as e:
                    return Response("phone number enter already exist",
                                    status=status.HTTP_406_NOT_ACCEPTABLE)
                StudentProfile.objects.create(standard_or_class=data.standard_or_class, user=user,
                                              pincode=data.pincode, phone_number=data.phone_number,
                                              email=data.email, last_name=data.last_name
                                              , first_name=data.first_name)
                data.delete()
                login(request, user)
                if user.email:
                    current_site = get_current_site(request)
                    MailVerification(user, current_site)
                    mail_otp = "please verify your mail also"
                else:
                    mail_otp = "it will be better if you also provide us your email address"
                x = {
                    'msg': "otp verififed, Account actiuated",
                    'mail_otp': mail_otp
                }
                return Response(x, status=status.HTTP_202_ACCEPTED)
            return Response("otp incorrect", status=status.HTTP_200_OK)
        return Response("otp expire", status=status.HTTP_200_OK)


# temperory teacher model till phone number verified
class TempTeacherView(APIView):

    def post(self, request):
        data = request.data
        try:
            t = TempTeacher.objects.get(phone_number=data['phone_number'])
            serializer = TempTeacherSerializer(t, data=data)

        except Exception:
            serializer = TempTeacherSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response("otp sent", status=status.HTTP_201_CREATED)
        return Response("something went wrong please retry", status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, ph_no):
        try:
            data = TempTeacher.objects.get(phone_number=ph_no)
        except exceptions.ObjectDoesNotExist:
            return Response("This phone number does not exist", status=status.HTTP_400_BAD_REQUEST)
        diff = datetime.now(timezone.utc) - data.date
        if diff.seconds > 20:
            data.otp = "1234"  # just a type of signal
            data.save()
            return Response("resend", status=status.HTTP_202_ACCEPTED)
        else:
            return Response("wait", status=status.HTTP_200_OK)


# do tranfering data and deleting in parallelism
# otp verify and tranfers user data,email verification if provided
class TeacherVerifyOtpView(APIView):
    def post(self, request):
        data_receive = request.data
        data = TempTeacher.objects.get(phone_number=data_receive['phone_number'])
        diff = datetime.now(timezone.utc) - data.date
        if diff.seconds < 5000:
            if data_receive["otp"] == data.otp:
                try:
                    user = User.objects.create_user(username=data.phone_number, email=data.email,
                                                    password=data.password, first_name=data.first_name,
                                                    last_name=data.last_name)
                except Exception as e:
                    return Response("phone number or email enter already exist",
                                    status=status.HTTP_406_NOT_ACCEPTABLE)
                TeacherProfile.objects.create(teacher_description=data.description, user=user
                                              ,  phone_number=data.phone_number,
                                              email=data.email, last_name=data.last_name,
                                              first_name=data.first_name)

                data.delete()
                login(request, user)
                if user.email:
                    current_site = get_current_site(request)
                    MailVerification(user, current_site)
                    mail_otp = "please verify your mail also"
                else:
                    mail_otp = "it will be better if you also provide us your email address"
                x = {
                    'msg': "otp verififed, Account actiuated",
                    'mail_otp': mail_otp
                }
                return Response(x, status=status.HTTP_202_ACCEPTED)
            return Response("OTP incorrect", status=status.HTTP_200_OK)
        return Response("OTP expire", status=status.HTTP_200_OK)

#class LoginView()