from django.conf.urls import url
from django.urls import path
from . import views
from . import views2
urlpatterns = [
    path('testing/', views.TestingView.as_view(), name='testing'),
    path('signup/s/', views.TempStudentView.as_view(), name='s_signup'),
    path('signup/t/', views.TempTeacherView.as_view(), name='t_signup'),
    path('<str:ph_no>/resend/s/', views.TempStudentView.as_view(), name='s_resend'),
    path('<str:ph_no>/resend/t/', views.TempTeacherView.as_view(), name='t_resend'),
    path('phone_number/verify/s/', views.StudentVerifyOtpView.as_view(), name='s_verify'),
    path('phone_number/verify/t/', views.TeacherVerifyOtpView.as_view(), name='t_verify'),
    path('profile/s/', views.StudetProfileView.as_view(), name='s_profile'),
    path('profile/t/', views.TeacherProfileView.as_view(), name='t_profile'),
    path('email/verification/<str:typ>/', views2.EmailVerificationView.as_view(), name='email_veriication'),

###- ---chaging important credetnial--------->>>>
    path('password/verification/<str:typ>/', views2.PasswordVerificationView.as_view()),
    path('change/credential/<str:uidb64>/<str:token>/<str:typ>/', views2.ChangeCredentialView.as_view()),
# ------Done ------>>>>>


    #path('password/otp/verify/<str:typ>', views2.PasswordResetOtpVerifyView.as_view(), name='otpverify'),#otl jaega
    path('password/verification/otp/<str:typ>/', views2.PasswordVerificationOtpView.as_view()),
    path('password_reset/', views2.PasswordResetView.as_view()),#otp jaega, without login
    #path('otp/login/', views2.otp_login_view,name='otplogin'),

    path('verify_email/<str:uidb64>/<str:token>/<str:type>/',views.activate_account, name='activate'),
    #path('new_password/<str:uidb64>/<str:token>/',views2.reset_password, name='email_newpassword')
    path('password_reset/new_password/', views2.NewPasswordView.as_view(), name='sms_newpassword'),
    #url(r'^new_password/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
     #   views2.reset_password, name='newpassword'),

]
