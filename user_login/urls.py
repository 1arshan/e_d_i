from django.urls import path
from . import views

urlpatterns = [
    path('homepage/s/', views.StudentHomePageView.as_view(), name='s_homepage'),

]