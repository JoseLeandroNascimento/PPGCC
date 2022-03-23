from django.urls import path
from upload.views import *;
from django.conf import settings
from django.conf.urls.static import static

app_name = "upload"

urlpatterns = [
    
    path('upload/',upload, name="upload"),
    path('salvar_arquivo/',salvar_arquivo,name="salvar_arquivo"),
    path("excluir_arquivo/<int:id>/",excluir_arquivo, name="excluir_arquivo"),
    path("excluir_tudo/",excluir_tudo, name="excluir_tudo"),
    path("buscar_arquivo/",buscarArquivo, name="buscar_arquivo"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

