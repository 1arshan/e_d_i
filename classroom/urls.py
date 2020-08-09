from django.urls import path
from . import views

urlpatterns = [
    path('institute/', views.InstituteView.as_view(), name='institute_view'),#only for admin
    path('institute/teacher/', views.InstituteTeacherView.as_view(), name='institute_teacher'),
    #path('institute/others/', views.InstituteOtherView.as_view(), name='institute_other'),#for anybody

]