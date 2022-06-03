from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.edit import DeleteView
from .models import Product
from .forms import ProductForm
from django.urls import reverse_lazy


# Create your views here.
class ProductListView(ListView):
    model = Product


class DetailProductView(DetailView):
    model = Product


class DeleteProductView(DeleteView):
    model = Product
    success_url = reverse_lazy('product_list')


class UpdateProductView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('product_list')


def search_product(request):
    if request.method == "POST":
        searched = request.POST['searched']
        products = Product.objects.filter(name__contains=searched)
        return render(request, 'search.html', {'searched': searched, 'products': products})
    else:
        return render(request, 'search.html')
