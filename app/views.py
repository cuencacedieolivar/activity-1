from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from .models import  Category, Product, Order , Review


class HomePageView(TemplateView):
    template_name = 'app/home.html'

class CategoryListView(ListView):
    model = Category
    template_name = 'app/category_list.html'
    context_object_name = 'categories'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'app/category_detail.html'
    context_object_name = 'category'

class ProductListView(ListView):
    model = Product
    template_name = 'app/product_list.html'
    context_object_name = 'product'

    def get_queryset(self):
        category = self.request.GET.get('category')
        if category:
            return Product.objects.filter(category__name=category)
        return Product.objects.all()

class ProductDetailView(DetailView):
    model = Product
    template_name = 'app/product_detail.html'
    context_object_name = 'products'

class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'category', 'price', 'description', 'stock', 'type', 'image']
    template_name = 'app/product_create.html'
    success_url = reverse_lazy('product_list')

class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'category', 'price', 'description', 'stock', 'type', 'image']
    template_name = 'app/product_update.html'
    success_url = reverse_lazy('product_list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'app/product_confirm_delete.html'
    success_url = reverse_lazy('product_list')

class OrderCreateView(CreateView):
    model = Order
    fields = ['product', 'quantity']
    template_name = 'app/order_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class OrderListView(ListView):
    model = Order
    template_name = 'app/order_list.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

class OrderDetailView(DetailView):
    model = Order
    template_name = 'app/order_detail.html'
    context_object_name = 'order'

class ReviewCreateView(CreateView):
    model = Review
    fields = ['rating', 'comment']
    template_name = 'app/review_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.product_id = self.kwargs['product_id']
        return super().form_valid(form)

class ReviewListView(ListView):
    model = Review
    template_name = 'app/review_list.html'
    context_object_name = 'reviews'

    def get_queryset(self):
        product_id = self.kwargs['product_id']
        return Review.objects.filter(product__id=product_id)