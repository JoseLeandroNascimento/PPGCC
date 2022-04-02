from django.urls import path
from inicio.views import *

urlpatterns = [

    path('',index),
    path('view-noticia/<int:noticia>',viewNoticia),
    path('view-noticias/',viewNoticias),
    path('view-defesas/',viewDefesas),
    path('view-defesa/<int:defesa_id>',viewDefesa),
    path('view-subsecao/<int:subsecao_id>',viewSecao)

]