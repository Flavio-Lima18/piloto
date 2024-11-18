from django.urls import path # type: ignore
from .views import index, sobre, contato
from . import views

urlpatterns = [
    path('', index, name='index'),
    path('sobre/', sobre, name='sobre'),
    path('contato/', contato, name='entrar_em_contato'),  
    path('item/<int:id>/', views.exibir_item, name='exibir_item'),
    path('perfil/<str:usuario>/', views.perfil, name='perfil'),
]
