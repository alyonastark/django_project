from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='категория')
    description = models.TextField(verbose_name='описание категории')

    def __str__(self):
        return f'{self.category_name}: {self.description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='наименование продукта')
    description = models.TextField(verbose_name='описание продукта')
    image = models.ImageField(upload_to='products/', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name='категория продукта', **NULLABLE)
    price = models.IntegerField(verbose_name='цена')
    created_at = models.DateTimeField(verbose_name='дата создания')
    updated_at = models.DateTimeField(verbose_name='дата последнего изменения')

    def __str__(self):
        return f'{self.product_name}: {self.price}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['product_name', 'price']


class Version(models.Model):
    product = models.ForeignKey(Product, related_name='version', on_delete=models.CASCADE, verbose_name='продукт')
    number = models.IntegerField(verbose_name='номер версии')
    name = models.CharField(max_length=150, verbose_name='название версии')
    is_current = models.BooleanField(default=False, verbose_name='текущая версия')

    def __str__(self):
        return f'версия {self.number}, {self.name}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'

