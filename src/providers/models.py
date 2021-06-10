from django.db import models
from products.models import ProviderProductModel


class ProviderModel(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    number_products = ProviderProductModel.objects.filter().count()

    def __str__(self) -> str:
        return self.name


    class Meta:
        verbose_name = 'provider'
        verbose_name_plural = 'providers'


