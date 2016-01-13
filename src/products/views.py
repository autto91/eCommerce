from django.shortcuts import render
from django.views.generic.detail import DetailView

# Create your views here.
from .models import Product

class ProducDetailView(DetailView):
    model = Product

def product_detail_view(reqeust, id):
    product_instance = Product.objects.get(id=id)
    template = 'product_detail.html'
    context = {
        'object': product_instance
    }
    return render(reqeust, template, context)