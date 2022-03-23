
from django.urls import path
from login.views import *  # NOQA

urlpatterns = [

    path("login/",login),
    path("logar/",logar),
    path("logout/",logout),
]