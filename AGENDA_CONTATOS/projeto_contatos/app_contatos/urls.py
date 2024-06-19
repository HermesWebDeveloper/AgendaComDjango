from django.urls import path
from app_contatos.views import NovoContato, ListaContatos, AtualizarContato, VisualizarContato, ExcluirContato
from app_contatos import views

urlpatterns = [
    path('', views.main, name='main'),

    path('novo_contato/', NovoContato.as_view(), name='novo_contato'),

    path('lista_contatos/', ListaContatos.as_view(), name='lista_contatos'),

    path('update/<int:pk>/', AtualizarContato.as_view(), name='update'),

    path('details/<int:pk>/', VisualizarContato.as_view(), name='details'),

    path('delete/<int:pk>/', ExcluirContato.as_view(), name='delete'),
]