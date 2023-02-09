from django.urls import path
from .views import *
urlpatterns = [
    path("register/", register, name = "register"),
    path("login/", loginUser, name = "login"),
    path("logout/", logoutUser, name = "logout"),
    path("accountUser/", accountUser, name = "accountUser"),
]
