from django.db import models
from django.core.validators import MinValueValidator


class ProductModel(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('categories.CategoryModel', on_delete=models.CASCADE)


class ProviderProductModel(models.Model):
    name = models.CharField(max_length=100)
    code = models.FloatField(validators=[MinValueValidator(0)])
    price = models.FloatField(validators=[MinValueValidator(0)])

    product = models.ForeignKey('products.ProductModel', on_delete=models.CASCADE)
    provide = models.ForeignKey('providers.ProviderModel', on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
