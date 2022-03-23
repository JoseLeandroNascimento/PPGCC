from django.urls import path
from secao.views import *

app_name = "secao"

urlpatterns = [
   path("addSecao/",addSecao),
   path("salvarSecao/",salvarSecao),
   path('editarSecao/<int:id>/',editarSecao,name="editarSecao"),
   path("updateSecao/",updateSecao),
   path("excluirSecao/",excluirSecao)
]
