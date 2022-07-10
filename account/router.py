from django.contrib import admin
from django.urls import path

from .views import login_view, logout_view, my_page_view

urlpatterns = [
    path("login/", login_view, name="login"),
    path("mypage/", my_page_view, name="my_page"),
    path("logout/", logout_view, name="logout")
]