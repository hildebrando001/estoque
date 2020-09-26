from django.urls import path
from projeto.produto import views

app_name = 'produto'

urlpatterns = [
    path('', views.produto_list, name='produto_list'),
    path('<int:pk>/', views.produto_detail, name='produto_detail'),
    path('add/', views.ProdutoCreate.as_view(), name='produto_add'),
]