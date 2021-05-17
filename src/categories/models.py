from django.db import models


class CategoryModel(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)


class ProviderCategoryModel(models.Model):
    url = models.URLField()
    provider = models.ForeignKey('providers.ProviderModel', on_delete=models.CASCADE)
    category = models.ForeignKey('categories.CategoryModel', on_delete=models.CASCADE)
