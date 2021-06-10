from django.db import models



class ProviderCategoryModel(models.Model):
    url = models.URLField()
    provider = models.ForeignKey('providers.ProviderModel', on_delete=models.CASCADE)
    category = models.ForeignKey('categories.CategoryModel', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'provider category'
        verbose_name_plural = 'provider categories'



class CategoryModel(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
