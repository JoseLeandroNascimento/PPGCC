from django.urls import path
from subsecao.views import *
urlpatterns = [
    path('subsecao-cadastro/<int:id_secao>',cadastroSubsecao)
]