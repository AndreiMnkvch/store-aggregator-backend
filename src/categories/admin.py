from django.contrib import admin
from categories.models import CategoryModel, ProviderCategoryModel
from products.models import ProductModel







class ProviderCategoryInLine(admin.TabularInline):
    model = ProviderCategoryModel
    extra = 1

class CategoryAdmin(admin.ModelAdmin):

    def count_number_products():
         return ProductModel.objects.all().count()


    def count_available_providers_number(self):
        return ProviderCategoryModel.objects.all().count()

    number_of_available_providers = count_available_providers_number()
    number_products = count_number_products()
    list_display = ('name', 'number_of_available_providers', 'number_products')
    inlines = (ProviderCategoryInLine,)







class ProviderCategoryAdmin(admin.ModelAdmin):
    fields = ('provider', 'url')



admin.site.register(ProviderCategoryModel,ProviderCategoryAdmin)
admin.site.register(CategoryModel,CategoryAdmin)


