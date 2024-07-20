from django.urls import path
from .views import UserRegisterView

urlpatterns = [
    path("signup/", UserRegisterView.as_view()), # post - 회원가입
]
