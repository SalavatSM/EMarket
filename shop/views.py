from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product, Category, User, Order, Address


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'

    def get_queryset(self):
        return Product.objects.all()


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'

    def get_queryset(self):
        return Product.objects.all()


class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'description', 'price', 'category', 'image']

    def get_queryset(self):
        return Product.objects.all()


class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'description', 'price', 'category', 'image']

    def get_queryset(self):
        return Product.objects.all()


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('product_list')

    def get_queryset(self):
        return Product.objects.all()


class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'

    def get_queryset(self):
        return Category.objects.all()


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category_detail.html'

    def get_queryset(self):
        return Category.objects.all()


class CategoryCreateView(CreateView):
    model = Category
    fields = ['name']

    def get_queryset(self):
        return Category.objects.all()


class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name']

    def get_queryset(self):
        return Category.objects.all()


class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('category_list')

    def get_queryset(self):
        return Category.objects.all()


class UserListView(ListView):
    model = User
    template_name = 'user_list.html'

    def get_queryset(self):
        return User.objects.all()


class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'

    def get_queryset(self):
        return User.objects.all()


class UserCreateView(CreateView):
    model = User
    fields = ['username', 'email', 'password']

    def get_queryset(self):
        return User.objects.all()


class UserUpdateView(UpdateView):
    model = User
    fields = ['username', 'email', 'password']

    def get_queryset(self):
        return User.objects.all()


class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('user_list')

    def get_queryset(self):
        return User.objects.all()


class OrderListView(ListView):
    model = Order
    template_name = 'order_list.html'

    def get_queryset(self):
        return Order.objects.all()


class OrderDetailView(DetailView):
    model = Order
    template_name = 'order_detail.html'

    def get_queryset(self):
        return Order.objects.all()


class OrderCreateView(CreateView):
    model = Order
    fields = ['user', 'created_at', 'updated_at', 'items', 'total_price']

    def get_queryset(self):
        return Order.objects.all()


class OrderUpdateView(UpdateView):
    model = Order
    fields = ['user', 'created_at', 'updated_at', 'items', 'total_price']

    def get_queryset(self):
        return Order.objects.all()


class OrderDeleteView(DeleteView):
    model = Order
    success_url = reverse_lazy('order_list')

    def get_queryset(self):
        return Order.objects.all()


class AddressListView(ListView):
    model = Address
    template_name = 'address_list.html'

    def get_queryset(self):
        return Address.objects.all()


class AddressDetailView(DetailView):
    model = Address
    template_name = 'address_detail.html'

    def get_queryset(self):
        return Address.objects.all()


class AddressCreateView(CreateView):
    model = Address
    fields = ['user', 'street', 'city', 'zip_code']

    def get_queryset(self):
        return Address.objects.all()


class AddressUpdateView(UpdateView):
    model = Address
    fields = ['user', 'street', 'city', 'zip_code']

    def get_queryset(self):
        return Address.objects.all()


class AddressDeleteView(DeleteView):
    model = Address
    success_url = reverse_lazy('address_list')

    def get_queryset(self):
        return Address.objects.all()


def index(request):
    return render(request, 'index.html')



