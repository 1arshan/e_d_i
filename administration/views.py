from django.shortcuts import render
from .serializers import CrashReportSerializers
from rest_framework import generics
from .models import CrashReport


class CrashReportView(generics.CreateAPIView):
    serializer_class = CrashReportSerializers
    queryset = CrashReport
