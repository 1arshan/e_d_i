from rest_framework import generics
from .serializers import *
from subject_material.models import VideoMaterial, Subject
from user_signup.models import StudentProfile, TeacherProfile
from rest_framework.permissions import IsAuthenticated
from .models import DoubtsQuestion
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


# ----home page of student will onlt see video available---->>
class StudentHomePageView(generics.ListAPIView):
    serializer_class = StudentHomePageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        t = StudentProfile.objects.get(user=self.request.user)
        return VideoMaterial.objects.filter(standard_link=t.standard_or_class,
                                            subject_link__field_name__contains=[t.course_field],
                                            teacher_link=TeacherProfile.objects.filter(is_verified=True)[:1])[:10]


# toic ,subject ---old version --GET request
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
                                            , teacher_link=TeacherProfile.objects.filter(is_verified=True)[:1])


# ----GET request --subject
class SubjectView(generics.ListAPIView):
    serializer_class = SubjectViewSerializer

    def get_queryset(self):
        t = StudentProfile.objects.get(user=self.request.user)
        return VideoMaterial.objects.filter(standard_link=t.standard_or_class,
                                            subject_link=self.request.GET['subject'],
                                            # teacher_link=TeacherProfile.objects.filter(is_verified=True)[:1],
                                            is_verified=True)


# ----GET request --subject, chapter
class ChapterView(generics.ListAPIView):
    serializer_class = ChapterSerializer

    def get_queryset(self):
        t = StudentProfile.objects.get(user=self.request.user)
        return VideoMaterial.objects.filter(standard_link=t.standard_or_class,
                                            subject_link=self.request.GET['subject'],
                                            chapter=self.request.GET['chapter'],
                                            # teacher_link=TeacherProfile.objects.filter(is_verified=True)[:1],
                                            is_verified=True)

# ----teacher view staterd

#----teacher home page ----->>>>>>
class TeacherHomePageView(generics.ListAPIView):
    serializer_class = TeacherHomePageSerializer

    def get_queryset(self):
        user =self.request.user
        return TeacherProfile.objects.all()



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
