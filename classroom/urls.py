from django.urls import path
from . import views

urlpatterns = [
    path('institute/', views.InstituteView.as_view(), name='institute_view'),#only for admin
    path('institute/teacher/', views.InstituteTeacherView.as_view(), name='institute_teacher'),
    #give institute_link of institute,pk for pk of techer profile
    path('institute/teacher/assosicated/', views.InstituteTeacherAssosiatedView.as_view(), name='institute_teacehr'),
    #intiute_info
    path('institute/class/',views.ClassView.as_view(), name='class'),#classes,pk of institute
    path('institute/class/admin/',views.ClassAdminView.as_view(), name='admin_class'),#classes,pk of institute for admin only

    path('assingment/',views.AssingmentView.as_view(), name='assingment'),#teacher to give assingment
    path('institute/others/', views.InstituteOtherView.as_view(), name='institute_other'),
    #for anybody

]