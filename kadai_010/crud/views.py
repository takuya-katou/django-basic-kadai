from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Product
from django.urls import reverse_lazy

class TopView(TemplateView):
    template_name = "top.html"

class ProductListView(ListView):
    model = Product
    paginate_by = 3

class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'

class ProductCreateView(CreateView): # あなたのView名に合わせてください
    model = Product
    fields = ['name', 'price'] # 例
    # 保存に成功した後の移動先を指定（例: 商品一覧画面）
    success_url = reverse_lazy('list') # 'list' は urls.py で定義した name

class ProductDetailView(DetailView):
    model = Product
    success_url = reverse_lazy('list')

class ProductUpdateView(UpdateView):
    model = Product
    fields = '__all__'
    template_name_suffix = '_update_form'

class ProductUpdateView(UpdateView): 
    model = Product
    fields = ['name', 'price'] # 例
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('list')

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('list')