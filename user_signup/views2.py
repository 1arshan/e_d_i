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
from broadcaster.mail import reset_otp_mail
from adcbackend.token import get_tokens_for_user, account_activation_token
from django.http import HttpResponse
from django.views.generic import View
from broadcaster.mail import MailVerification
from django.shortcuts import render
from .forms import PasswordChangeForm
from django.core.exceptions import MultipleObjectsReturned


# from braodcaster.tasks import send_parallel_mail


# password reset ----------> username ,medium ,type
class PasswordResetView(APIView):
    permission_classes = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.otp = random.randrange(10101, 909090) -----this nedd to be updated
        self.otp = "1234"

    def post(self, request):
        data = request.data
        if data['medium'] == 'sms':
            content = "verification code is: " + str(self.otp) + "\nthis code will valid for only 60 secs"
            broadcast_sms(data['username'], content)
            try:
                if data['type'] == 's':
                    temp = StudentProfile.objects.get(phone_number=data['username'])
                    temp.otp = self.otp
                    temp.save()

                else:
                    temp = TeacherProfile.objects.get(phone_number=data['username'])
                    temp.otp = self.otp
                    temp.save()

            except Exception:
                x = {'msg': "otp send to your number ,if not receive please check mobile number entered"}
                return Response(x, status=status.HTTP_200_OK)

            x = {'msg': "otp send to your number ,if not receive please check mobile number entered"}
            return Response(x, status=status.HTTP_200_OK)

        elif data['medium'] == 'email':
            try:
                user = User.objects.get(email=data['username'])
                reset_otp_mail(user)

            except MultipleObjectsReturned:
                x = {'msg': "More than one account is link with this email so password cannot be reset by email try "
                            "sms method"}
                return Response(x, status=status.HTTP_200_OK)

            except Exception as e:
                x = {'msg': "One time link is send to your email if not receive please check email address enter"}
                return Response(x, status=status.HTTP_200_OK)

            x = {'msg': "One time link is send to your email if not receive please check email address enter"}
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
                if data['otp'] == t.studentprofile.otp and diff.seconds < 60:
                    x = get_tokens_for_user(t)
                    x["msg"] = "Otp is correct"
                    return Response(x, status=status.HTTP_200_OK)
                else:
                    x = {'msg': "either otp provided is wrong or it expires"}
                    return Response(x, status=status.HTTP_200_OK)

            else:
                diff = datetime.now(timezone.utc) - t.teacherprofile.date
                if data['otp'] == t.teacherprofile.otp and diff.seconds < 60:
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
class EmailResetPasswordView(View):
    form_class = PasswordChangeForm
    template_name = 'UserSignup/change_password.html'

    # display blank form
    def get(self, request, uidb64, token):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request, uidb64, token):
        try:
            uid = force_bytes(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            return HttpResponse('Activation link is invalid!', status=status.HTTP_400_BAD_REQUEST)
        if user is not None and account_activation_token.check_token(user, token):
            form = PasswordChangeForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                if data['new_password'] == data['confirm_password']:
                    user.set_password(data['new_password'])
                    user.save()
                else:

                    return render(request, 'UserSignup/change_password.html', {'msg': 'Password enter does not match '
                                                                                      'with confirm password',
                                                                               'form': form})
                return HttpResponse('Your password has been reset,Login in the app to access your account',
                                    status=status.HTTP_201_CREATED)
            return render(request, 'UserSignup/change_password.html', {'msg': 'data enter is not valid',
                                                                       'form': form})
        else:
            return HttpResponse('link is invalid!', status=status.HTTP_400_BAD_REQUEST)


# password check and otl send, when user is already login
class PasswordVerificationView(APIView):

    def post(self, request, typ):
        data = request.data
        user = self.request.user
        if user.check_password(data['password']):
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = account_activation_token.make_token(user)
            link = 'http://ec2-13-126-196-234.ap-south-1.compute.amazonaws.com/' + 'user/change/credential/' + \
                   uid + '/' + token + '/' + typ + "/"
            x = {'otl': link,
                 'msg': 'passwprd correct'}
            return Response(x, status=status.HTTP_200_OK)
        x = {'msg': 'password incorrect'}
        return Response(x, status=status.HTTP_200_OK)


# type-----otp send to sms
class PasswordVerificationOtpView(APIView):

    def get(self, request, typ):
        user = self.request.user
        otp = random.randrange(10101, 909090)
        content = "verification code is: " + str(otp) + "\nthis code will valid for only 60 secs"
        broadcast_sms(user.username, content)
        if typ == 's':

            user.studentprofile.otp = otp
            user.studentprofile.save()
        else:
            user.teacherprofile.otp = otp
            user.teacherprofile.save()
        x = {'msg': 'otp send'}
        return Response(x, status=status.HTTP_200_OK)


# ----give 'data' and 'field' and change credential
class ChangeCredentialView(APIView):

    def post(self, request, uidb64, token, typ):
        try:
            data = request.data
            uid = force_bytes(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            return HttpResponse('link is invalid!', status=status.HTTP_200_OK)
        if user is not None and account_activation_token.check_token(user, token):

            if data['field'] == 'password':
                user.set_password(data['data'])
                user.save()
            elif data['field'] == 'email':
                user.email = data['data']
                user.save()
                if typ == 't':
                    user.teacherprofile.email = data['data']
                    user.teacherprofile.save()
                else:
                    user.studentprofile.email = data['data']
                    user.studentprofile.save()

            elif data['field'] == 'phone_number':
                user.username = data['data']
                user.save()
                if typ == 't':
                    TeacherProfile.objects.filter(user=user).update(phone_number=data['data'])

                else:

                    StudentProfile.objects.filter(user=user).update(phone_number=data['data'])

            x = {'msg': data['field'] + " change"}
            return Response(x, status=status.HTTP_201_CREATED)
        else:
            x = {'msg': "link is invalid"}
            return Response(x, status=status.HTTP_200_OK)


class EmailVerificationView(APIView):

    def get(self, request, typ):
        user = self.request.user
        MailVerification(user, type=typ)
        x = {'msg': "verification mail is send to your email"}
        return Response(x, status=status.HTTP_200_OK)
