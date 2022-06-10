from django.urls import path
from . import views
from .views import UserDetailAPI,RegisterUserAPIView,RegisterAPI

urlpatterns = [
	path('', views.index, name="index"),
	path('register/', RegisterAPI.as_view(), name='register'),
]