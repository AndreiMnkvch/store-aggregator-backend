from django.db import models


class CategoryModel(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class ProviderCategoryModel(models.Model):
    url = models.URLField()
    provider = models.ForeignKey('providers.ProviderModel', on_delete=models.CASCADE)
    category = models.ForeignKey('categories.CategoryModel', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.category, self.provider

    class Meta:
        verbose_name = 'provider category'
        verbose_name_plural = 'provider categories'
