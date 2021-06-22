from django.contrib import admin

from products.models import ProviderProductModel
from providers.models import ProviderModel


class ProviderProductInLine(admin.StackedInline):
    model = ProviderProductModel
    extra = 0
    min_num = 0


class ProviderAdmin(admin.ModelAdmin):
    inlines = (ProviderProductInLine,)
    list_display = ('name', 'number_products')

    def number_products(self, obj):
        return obj.providerproductmodel_set.count()


admin.site.register(ProviderModel, ProviderAdmin)
