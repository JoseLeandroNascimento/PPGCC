from django.urls import path
from noticias.views import *

urlpatterns = [
    path("noticias/", noticias),
    path("add_noticia/", add_noticia),
    path("salvar_noticia/", salvar_noticia),
    path("excluir_noticia/", excluir_noticia),
    path("editar_noticia/", editar_noticia),
    path("update_noticia/", update_noticia),
    path("buscar_noticia/",buscarNoticia),
 
]
