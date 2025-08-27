from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ProfileViewSet, RegisterView, LoginView

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'profiles', ProfileViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
]
