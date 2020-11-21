from django.shortcuts import render
from django.views.generic import DetailView
from .models import Goods

def welcome(request):
    return render(request, 'goodsdetail/welcome.html')

class GoodsDetailView(DetailView):
    model = Goods
    template_name = 'goodsdetail/Product.html'
    context_object_name = 'product'