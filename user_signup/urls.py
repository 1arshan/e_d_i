from django.conf.urls import url
from django.urls import path
from . import views
#from . import views2
urlpatterns = [
    path('signup/s/', views.TempStudentView.as_view(), name='s_signup'),
    path('signup/t/', views.TempTeacherView.as_view(), name='t_signup'),
    path('<str:ph_no>/resend/s/', views.TempStudentView.as_view(), name='s_resend'),
    path('<str:ph_no>/resend/t/', views.TempTeacherView.as_view(), name='t_resend'),
    path('phone_number/verify/s/', views.StudentVerifyOtpView.as_view(), name='s_verify'),
    path('phone_number/verify/t/', views.TeacherVerifyOtpView.as_view(), name='t_verify'),
    path('profile/s/', views.StudetProfileView.as_view(), name='s_profile'),
    path('profile/t/', views.TeacherProfileView.as_view(), name='t_profile'),
    #path('login', views.LoginView.as_view(), name='login'),
    #path('password_reset/<str:medium>/', views2.PasswordResetView.as_view()),
    #path('otp/login/', views2.otp_login_view,name='otplogin'),
    #path('password_reset/otp/verify/', views2.PasswordResetOtpVerifyView.as_view(), name='otpverify'),
    path('verify_email/<str:uidb64>/<str:token>/<str:type>/',views.activate_account, name='activate')
    #url(r'^verify_email/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
     #   views.activate_account, name='activate'),
    #url(r'^new_password/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
     #   views2.reset_password, name='newpassword'),

]
