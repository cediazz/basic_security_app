from django.urls import path,include
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [
    path('login/',TokenObtainPairView.as_view()),
    path('refresh-token/',TokenRefreshView.as_view()),
]