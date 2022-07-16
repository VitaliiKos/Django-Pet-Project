from django.db import models
from django.core import validators


class CategoryModel(models.Model):
    class Meta:
        ordering = ('name',)
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'

    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    def __str__(self):
        return self.name.capitalize()


class ProductModel(models.Model):
    class Meta:
        ordering = ('name',)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукти'

        # index_together = (('id', 'slug'),)

    category = models.ForeignKey(CategoryModel, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True, validators=(
        validators.MaxLengthValidator(200),
        validators.MinLengthValidator(2)
    ))
    # slug = models.SlugField(max_length=200, db_index=True, blank=True, validators=(
    #     validators.MaxLengthValidator(200),
    #     validators.MinLengthValidator(2)
    # ))
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)

    price = models.DecimalField(max_digits=10, decimal_places=2, validators=(
        validators.MaxValueValidator(1000000),
        validators.MinValueValidator(1)
    ))
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name.capitalize()
