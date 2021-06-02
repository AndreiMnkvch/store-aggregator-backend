from django.contrib import admin
from categories.models import CategoryModel, ProviderCategoryModel

class ProviderCategoryInLine(admin.TabularInline):
    model = ProviderCategoryModel
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'number_of_available_providers','number_products')
    inlines = [ProviderCategoryInLine]




class ProviderCategoryAdmin(admin.ModelAdmin):
    fields = ['provider', 'url']



admin.site.register(ProviderCategoryModel,ProviderCategoryAdmin)
admin.site.register(CategoryModel,CategoryAdmin)


