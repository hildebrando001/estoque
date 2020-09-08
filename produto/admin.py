from django.contrib import admin
from .models import Produto

@admin.register(Produto) #admin.site.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):   # Desenhou um layout com lista de produtos
    list_display = (                    # admin/produto/produto
        '__str__',
        'importado',
        'ncm',
        'preco',
        'estoque',
        'estoque_minimo',
    )
    search_fields = ('produto',)
    list_filter = ('importado',)