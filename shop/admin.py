from django.contrib import admin
from .models import Product, User, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'is_active')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'pk')


admin.site.register(Product, ProductAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Category, CategoryAdmin)


