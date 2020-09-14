from django.shortcuts import render
from .models import Produto


def produto_list(request):
    objects = Produto.objects.all()
    return render(request, 'produto_list.html', {'object_list': objects})


def produto_detail(request, pk):
    obj = Produto.objects.get(pk=pk)
    return render(request, 'produto_detail.html', {'object': obj})

def produto_add(request):
    return render(request, 'produto_form.html')