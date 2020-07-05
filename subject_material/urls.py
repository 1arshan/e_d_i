from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.StudyMaterialUploadView.as_view(), name='upload'),

]