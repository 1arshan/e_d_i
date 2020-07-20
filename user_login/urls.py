from django.urls import path
from . import views
from subject_material.views import TeacherChapterView,TeacherChapterNotesView

urlpatterns = [
    path('homepage/s/', views.StudentHomePageView.as_view(), name='s_homepage'),#show random 10 vidoes
    path('homepage/t/', views.TeacherHomePageView.as_view(), name='t_homepage'),#his selected subject
    path('subject/s/', views.StudentSubjectView.as_view(), name='s_subject'),# chapter in that subject
    path('subject/t/', views.TeacherSubjectView.as_view(), name='t_subject'),# chapter in that subject+class
    path('chapter/s/', views.StudentChapterView.as_view(), name='s_chapter'),# material in that chapter
    path('chapter/t/', TeacherChapterView.as_view(), name='t_chapter'),#material in that chapter+POST
    path('chapter/notes/t/', TeacherChapterNotesView.as_view(), name='t_chapter'),#material in that chapter+POST
    path('material/s/', views.StudentMaterialView.as_view(), name='t_chapter'),#material in that chapter+POST
    path('querry/s/', views.StudentQuerryView.as_view(), name='s_homepage'),
    path('doubts/<str:pk>/s/', views.DoubtsQuestionView.as_view(), name='doubts'), #video material ka pk hai
    #path('ask_doubts/video/<str:pk>/', views.DoubtsQuestionView.as_view(), name='doubts'),
    path('doubts/unans/', views.QuesToBeAnsView.as_view(), name='all_doubts'),
    #specific teacher,question whci is not answer
    path('doubts/ans/', views.QuesWhichIsAnsView.as_view(), name='all_ans_doubts'),
    #specific teacher,question which is ans
    
]