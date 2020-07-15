from django.urls import path
from . import views

urlpatterns = [
    path('homepage/s/', views.StudentHomePageView.as_view(), name='s_homepage'),
    path('subject/s/', views.SubjectView.as_view(), name='s_subject'),
    path('chapter/s/', views.ChapterView.as_view(), name='s_chapter'),
    path('querry/s/', views.StudentQuerryView.as_view(), name='s_homepage'),
    path('doubts/<str:pk>/s/', views.DoubtsQuestionView.as_view(), name='doubts'), #video material ka pk hai
    #path('ask_doubts/video/<str:pk>/', views.DoubtsQuestionView.as_view(), name='doubts'),
    path('doubts/unans/', views.QuesToBeAnsView.as_view(), name='all_doubts'),
    #specific teacher,question whci is not answer
    path('doubts/ans/', views.QuesWhichIsAnsView.as_view(), name='all_ans_doubts'),
    #specific teacher,question which is ans
    
]