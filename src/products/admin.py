from django.contrib import admin
from .models import ProductModel,ProviderProductModel


class ProviderProductAdmin(admin.ModelAdmin):
    fields = ['name', 'code', 'price', 'provider']
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category',)
    list_filter = ['category']
    search_fields = ['name']



admin.site.register(ProviderProductModel)
admin.site.register(ProductModel, ProductAdmin)




