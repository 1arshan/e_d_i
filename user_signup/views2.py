from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import StudentProfile, TeacherProfile
from datetime import datetime, timezone
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.models import User
from broadcaster.sms import broadcast_sms
from broadcaster.mail import broadcast_mail
from django.core.exceptions import ObjectDoesNotExist
import random
from django.db.models import Q
from django.utils.http import urlsafe_base64_encode
from rest_framework.decorators import api_view
from broadcaster.mail import reset_otp_mail
from adcbackend.token import get_tokens_for_user, account_activation_token
from django.http import HttpResponse
from django.views.generic import View

# from braodcaster.tasks import send_parallel_mail


# password reset ----------> username ,medium ,type
class PasswordResetView(APIView):
    permission_classes = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.otp = random.randrange(10101, 909090)

    def post(self, request):
        data = request.data
        if data['medium'] == 'sms':
            content = "verification code is: " + str(self.otp) + "\nthis code will valid for only 60 secs"
            broadcast_sms(data['username'], content)
            try:
                if data['type'] == 's':

                    StudentProfile.objects.filter(phone_number=data['username']).update(otp=self.otp)
                else:
                    TeacherProfile.objects.filter(phone_number=data['username']).update(otp=self.otp)
            except Exception:
                x = {'msg': "otp send to your number ,if not receive please check mobile number entered"}
                return Response(x, status=status.HTTP_200_OK)

            x = {'msg': "otp send to your number ,if not receive please check mobile number entered"}
            return Response(x, status=status.HTTP_200_OK)

        elif data['medium'] == 'email':

            try:
                user = User.objects.get(email__iexact=data['username'])
                reset_otp_mail(user)

            except Exception as e:
                x = {'msg': "One time link is send to your email if not receive please cheack email address enter"}
                return Response(x, status=status.HTTP_200_OK)

            x = {'msg': "One time link is send to your email if not receive please cheack email address enter"}
            return Response(x, status=status.HTTP_200_OK)


# reset password otp send verification  username,otp,type
class PasswordResetOtpVerifyView(APIView):
    permission_classes = []

    def post(self, request):
        data = request.data
        try:
            t = User.objects.get(Q(username=data['username']))

            if data['type'] == 's':
                diff = datetime.now(timezone.utc) - t.studentprofile.date
                if data['otp'] == t.studentprofile.otp and diff.seconds < 60000:
                    x = get_tokens_for_user(t)
                    x["msg"] = "Otp is correct"
                    return Response(x, status=status.HTTP_200_OK)
                else:
                    x = {'msg': "either otp provided is wrong or it expires"}
                    return Response(x, status=status.HTTP_200_OK)

            else:
                diff = datetime.now(timezone.utc) - t.teacherprofile.date
                if data['otp'] == t.teacherprofile.otp and diff.seconds < 60000:
                    x = get_tokens_for_user(t)
                    x["msg"] = "Otp is correct"
                    return Response(x, status=status.HTTP_200_OK)
                else:
                    x = {'msg': "either otp provided is wrong or it expires"}
                    return Response(x, status=status.HTTP_200_OK)
        except ObjectDoesNotExist or Exception:
            x = {'msg': "either otp provided is wrong or it expires"}
            return Response(x, status=status.HTTP_200_OK)


# password change ------token,new password
class NewPasswordView(APIView):
    def post(self, request):
        data = request.data
        t = User.objects.get(username=self.request.user.username)
        t.set_password(data['password'])
        t.save()
        x = {'msg': "password change"}
        return Response(x, status=status.HTTP_200_OK)


# inserting new password
class ResetPasswordView(View):
    model = StudentProfile
    template_name = 'EClass/premium.html'

    def post(self, request, uidb64, token):
        try:
            uid = force_bytes(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            return HttpResponse('Activation link is invalid!', status=status.HTTP_400_BAD_REQUEST)
        if user is not None and account_activation_token.check_token(user, token):
            data = request.data
            if data['new_password'] == data['confirm_password']:
                user.set_password(data['new_password'])
                user.save()
            else:
                return HttpResponse('new password and confirm password are not same', status=status.HTTP_201_CREATED)
            return HttpResponse('Password Reset', status=status.HTTP_201_CREATED)
        else:
            return HttpResponse('link is invalid!', status=status.HTTP_400_BAD_REQUEST)
