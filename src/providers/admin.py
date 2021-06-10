from django.contrib import admin
from providers.models import ProviderModel
from products.models import ProviderProductModel

class ProviderProductInLine(admin.TabularInline):
    model = ProviderProductModel
    extra = 0


class ProviderAdmin(admin.ModelAdmin):
    inlines = (ProviderProductInLine,)
    list_display = ('name', 'number_products')

admin.site.register(ProviderModel,ProviderAdmin)

