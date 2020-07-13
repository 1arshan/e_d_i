from rest_framework import generics
from .serializers import *
from subject_material.models import VideoMaterial
from user_signup.models import StudentProfile,TeacherProfile
from rest_framework.permissions import IsAuthenticated
from .models import DoubtsQuestion


# ----home page of student will onlt see video available---->>
class StudentHomePageView(generics.ListAPIView):
    serializer_class = StudentHomePageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return VideoMaterial.objects.filter(standard_link=StudentProfile.objects.get
        (user=self.request.user).standard_or_class,teacher_link=TeacherProfile.objects.filter(is_verified=True)[:1])[:10]


class StudentQuerryView(generics.ListAPIView):
    serializer_class = StudentHomePageSerializer

    def get_queryset(self):
        data = self.request.data
        standard_link = StudentProfile.objects.get(user=self.request.user).standard_or_class
        subject = data['subject']
        if data['topic']:
            topic = data['topic']
            return VideoMaterial.objects.filter(standard_link=standard_link, subject_link=subject,
                                                topic__iexact=topic,
                                                teacher_link=TeacherProfile.objects.filter(is_verified=True)[:1])

        return VideoMaterial.objects.filter(standard_link=standard_link, subject_link=subject
                                            ,teacher_link=TeacherProfile.objects.filter(is_verified=True)[:1])


# ----Doubts quesiton section, specific to video material--->
class DoubtsQuestionView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = 'pk'
    lookup_field = 'material_link'
    serializer_class = DoubtsQuestionSerializer

    def get_queryset(self):
        return DoubtsQuestion.objects.filter(material_link=self.kwargs['pk'])


# -----view all question that teacher ians------>>>>>
class QuesToBeAnsView(generics.ListAPIView):
    serializer_class = DoubtsQuestionSerializer

    def get_queryset(self):
        user = self.request.user.username
        return DoubtsQuestion.objects.filter(teacher_link=user, is_answered=False)


class QuesWhichIsAnsView(generics.ListAPIView):
    serializer_class = DoubtsQuestionSerializer

    def get_queryset(self):
        user = self.request.user.username
        return DoubtsQuestion.objects.filter(teacher_link=user, is_answered=True)
