from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Blog.urls')),  # Carrega as URLs do Blog diretamente no root
]
