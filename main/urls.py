
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('home.urls')),
    path('', include('usuario.urls')),
    path('',include('secao.urls')),
    path('',include('defesa.urls')),
    path('', include('upload.urls')),
    path('', include('noticias.urls')),
    path('',include('login.urls')),
    path('', include('subsecao.urls'))

]
