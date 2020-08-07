from django.urls import path
from . import views

urlpatterns = [
    path('crash/report/', views.CrashReportView.as_view(), name='crash_report'),


]