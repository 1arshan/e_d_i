from rest_framework import generics
from .serializers import *
from subject_material.models import VideoMaterial
from user_signup.models import StudentProfile
from rest_framework.permissions import IsAuthenticated
from .models import DoubtsQuestion

#----home page of student will onlt see video available---->>
class StudentHomePageView(generics.ListAPIView):
    serializer_class = StudentHomePageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return VideoMaterial.objects.filter(standard_link=StudentProfile.objects.get
        (user=self.request.user).standard_or_class)


#----Doubts quesiton section, specific to question--->
class DoubtsQuestionView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = 'pk'
    lookup_field = 'material_link'
    serializer_class = DoubtsQuestionSerializer

    def get_queryset(self):
        return DoubtsQuestion.objects.filter(material_link=self.kwargs['pk'])

