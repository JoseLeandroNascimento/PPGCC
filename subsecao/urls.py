from django.urls import path
from subsecao.views import *
urlpatterns = [
    path('subsecao-cadastro/<int:id_secao>',cadastroSubsecao),
    path('subsecao-salvar/',salvarSubsecao),
    path('subsecao-view/<int:id_subsecao>',subsecao)
]