from django.urls import path
from subsecao.views import *
urlpatterns = [
    path('subsecao-cadastro/<int:id_secao>',cadastroSubsecao),
    path('subsecao-salvar/',salvarSubsecao),
    path('subsecao-view/<int:id_subsecao>',subsecao),
    path('subsecao-editar/',subsecaoEditar),
    path('subsecao-configurar/',configurar),
    path('subsecao-update/',updateSubsecao),
    path('subsecao-atualizar/',atualizarSubsecao),
    path('subsecao-delete/',delete),
    path('subsecao-clear/',subsecaoClear)
]