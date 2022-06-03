from django.urls import path
from products.views import ProductListView, DetailProductView,DeleteProductView,UpdateProductView,search_product

urlpatterns = [
    path('', ProductListView.as_view(template_name="base.html"),name='product_list'),
    path('search',search_product,name='product_search'),
    path('prod/<int:pk>', DetailProductView.as_view(template_name="product_detail.html"), name='product_detail'),
    path('edit/<int:pk>', UpdateProductView.as_view(template_name="product_edit.html"), name='product_edit'),
    path('delete/<int:pk>', DeleteProductView.as_view(template_name="product_delete.html"), name='product_delete'),

]
