from django.contrib import admin
from categories.models import CategoryModel, ProviderCategoryModel

admin.site.register(ProviderCategoryModel)
admin.site.register(CategoryModel)

