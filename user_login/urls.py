from django.urls import path
from . import views

urlpatterns = [
    path('homepage/s/', views.StudentHomePageView.as_view(), name='s_homepage'),
    path('doubts/<str:pk>/', views.DoubtsQuestionView.as_view(), name='doubts'), #video material ka pk hai

]