from django.contrib import admin
from categories.models import CategoryModel, ProviderCategoryModel


class ProviderCategoryInLine(admin.StackedInline):
    extra = 0
    min_num = 1
    model = ProviderCategoryModel


class ProviderCategoryAdmin(admin.ModelAdmin):
    fields = ('provider', 'url')


class CategoryAdmin(admin.ModelAdmin):

    def available_providers_number(self, obj):
        return obj.providercategorymodel_set.count()

    def number_products(self, obj):
        return obj.productmodel_set.count()

    inlines = (ProviderCategoryInLine,)
    list_display = ('name', 'number_products', 'available_providers_number',)


admin.site.register(CategoryModel, CategoryAdmin)
admin.site.register(ProviderCategoryModel, ProviderCategoryAdmin)
