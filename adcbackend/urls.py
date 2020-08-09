from rest_framework_simplejwt import views as jwt_views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user_signup.urls')),
    path('user_login/', include('user_login.urls')),
    path('study_material/',include('subject_material.urls')),
    path('administration/', include('administration.urls')),
    path('classroom/', include('classroom.urls')),

    #django inbuild
    path('api-auth/', include('rest_framework.urls')),

    # jwt login
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
