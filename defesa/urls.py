
from django.urls import path
from defesa.views import *

urlpatterns = [

    path("defesa/",defesa),
    path("cadatrarDefesa/",cadatroDefesa),
    path("salvarDefesa/",salvarDefesa),
    path("excluirDefesa/",excluirDefesa),
    path("busca_defesas/",buscarDefesas),
    path("editarDefesa/",editarDefesa),
    path('updateDefesa/',updateDefesa)
    
]
