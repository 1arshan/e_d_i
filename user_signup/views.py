from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import TempStudent, StudentProfile, TempTeacher, TeacherProfile
from .serializers import TempStudentSerializer, TempTeacherSerializer, StudentSerializer, TeacherSerializer
from datetime import datetime, timezone
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from broadcaster.mail import MailVerification
from django.contrib.auth import login
from django.core import exceptions
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from adcbackend.token import get_tokens_for_user


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
    permission_classes = []

    def post(self, request):
        data_receive = request.data
        data = TempStudent.objects.get(phone_number=data_receive['phone_number'])
        diff = datetime.now(timezone.utc) - data.date
        if diff.seconds < 5000:
            if data_receive["otp"] == data.otp:
                try:
                    user = User.objects.create_user(username=data.phone_number, email=data.email,
                                                    password=data.password, first_name=data.first_name,
                                                    last_name=data.last_name)
                except Exception as e:
                    return Response("user with this phone number already exist",
                                    status=status.HTTP_406_NOT_ACCEPTABLE)
                try:

                    StudentProfile.objects.create(standard_or_class=data.standard_or_class, user=user,
                                                  pincode=data.pincode, phone_number=data.phone_number,
                                                  email=data.email, last_name=data.last_name
                                                  , first_name=data.first_name)
                except Exception as e:
                    return Response("phone number enter already exist",
                                    status=status.HTTP_406_NOT_ACCEPTABLE)
                data.delete()
                if user.email:
                    # current_site = get_current_site(request)
                    # MailVerification(user, current_site)
                    mail_otp = "please verify your mail also"
                else:
                    mail_otp = "it will be better if you also provide us your email address"

                x = get_tokens_for_user(user)
                x["message"] = "otp verififed, Account actiuated"
                x['mail'] = mail_otp
                return Response(x, status=status.HTTP_202_ACCEPTED)
            return Response("otp incorrect", status=status.HTTP_200_OK)
        return Response("otp expire", status=status.HTTP_200_OK)


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
    permission_classes = []

    def post(self, request):
        data_receive = request.data
        data = TempTeacher.objects.get(phone_number=data_receive['phone_number'])
        diff = datetime.now(timezone.utc) - data.date
        if diff.seconds < 500:
            if data_receive["otp"] == data.otp:
                try:
                    user = User.objects.create_user(username=data.phone_number, email=data.email,
                                                    password=data.password, first_name=data.first_name,
                                                    last_name=data.last_name)


                except Exception as e:
                    return Response("user with this phone number already exist",
                                    status=status.HTTP_406_NOT_ACCEPTABLE)

                try:
                    TeacherProfile.objects.create(teacher_description=data.description, user=user
                                                  , phone_number=data.phone_number,
                                                  email=data.email, last_name=data.last_name,
                                                  first_name=data.first_name)

                except Exception as e:
                    user.delete()
                    return Response("user with this email already exist",
                                    status=status.HTTP_406_NOT_ACCEPTABLE)

                data.delete()
                login(request, user)
                if user.email:
                    # current_site = get_current_site(request)
                    # MailVerification(user, current_site)
                    mail_otp = "please verify your mail also"
                else:
                    mail_otp = "it will be better if you also provide us your email address"

                x = get_tokens_for_user(user)
                x["message"] = "otp verififed, Account actiuated"
                x['mail'] = mail_otp
                return Response(x, status=status.HTTP_202_ACCEPTED)
            return Response("OTP incorrect", status=status.HTTP_200_OK)
        return Response("OTP expire", status=status.HTTP_200_OK)


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
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# --student profile view and change,user model has not change-->>>
class TeacherProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = TeacherSerializer(TeacherProfile.objects.get(phone_number=self.request.user.username))
        return Response(serializer.data)
