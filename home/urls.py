from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
]

    # path('', views.index, name='index'),
    # path('sobre/', views.sobre, name='sobre'),
    # path('contato/', views.contato, name='entrar_em_contato'),  
    # path('item/<int:id>/', views.exibir_item, name='exibir_item'),
    # path('perfil/<str:usuario>/', views.perfil, name='perfil'),
    # path('dia_da_semana/<int:numero>/', views.dia_da_semana, name='dia_da_semana'),

