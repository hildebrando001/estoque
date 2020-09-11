from django.shortcuts import render
from .models import Produto


def produto_list(request):
    objects = Produto.objects.all()
    return render(request, 'produto_list.html', {'object_list': objects})