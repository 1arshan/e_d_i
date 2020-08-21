from django.urls import path
from . import views, views2

urlpatterns = [
    path('institute/', views.InstituteView.as_view(), name='institute_view'),  # only for admin
    path('institute/teacher/', views.InstituteTeacherView.as_view(), name='institute_teacher'),
    # give institute_link of institute,pk for pk of techer profile ONLY for admin
    path('institute/teacher/info/', views.InstituteTeacherInfoView.as_view(), name='institute_teacher_info'),
    #---for non admin
    path('institute/teacher/assosicated/', views.InstituteTeacherAssosiatedView.as_view(), name='institute_teacehr'),
    # intiute_info
    path('institute/class/', views.ClassView.as_view(), name='class'),  # classes,pk of institute
    path('institute/class/admin/', views.ClassAdminView.as_view(), name='admin_class'),
    # classes,pk of institute for admin only

    path('teacher/student/', views.TeacherStudentView.as_view(), name='t-s'),
    # teacehr to see student in the class
    path('assingment/', views.AssingmentView.as_view(), name='assingment'),  # teacher to give assingment
    path('assingment/admin/', views.AssingmentAdminView.as_view(), name='admin_assingment'),
    # Admin to oversee all classes

    path('assingment/submitted/', views.AssingmentSubmittedView.as_view(), name='t-ass-sub'),
    # tacher to see assignment submitted in a class
    path('assingment/admin/submitted/', views.AssingmentAdminSubmittedView.as_view(), name='ad-ass-sub'),
    # tacher to see assignment submitted in a class

    path('institute/others/', views.InstituteOtherView.as_view(), name='institute_other'),
    # for anybody

    # --student----->>>>>
    path('student/', views2.StudentClassView.as_view(), name='studetn_class'),
    path('student/classmate/', views2.StudentClassmateView.as_view(), name='studetn_classmate'),
    path('student/assignment/', views2.StudentAssignmentView.as_view(), name='studnet_assng'),
    path('student/assignment/submission/', views2.StudentAssignmentSubmissionView.as_view(), name='submission'),

]
