from django.urls import path
from . import views
#from . import views2
urlpatterns = [
    path('homepage/s/', views.StudentHomePageView.as_view(), name='s_homepage'),

]