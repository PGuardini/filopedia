"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from cards import views

#
# NECESSÁRIO: ISOLAR ROTA ADMIN/
#

# Routers
router = routers.DefaultRouter()
router.register(r'filosofos', views.FilosofoView, 'filosofo')
router.register(r'exibicoes', views.ExibicaoView, 'exibicao')

urlpatterns = [
    # atribui à rota "admin/" o site de admin
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),


    # puxa as urls do app cards e posiciona elas na rota index do projeto
    path('', include('cards.urls')),
]
