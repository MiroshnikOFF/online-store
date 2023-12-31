from django.db import models

from config import settings

NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = "Категории"


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    image = models.ImageField(**NULLABLE, upload_to='images/', verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена за покупку')
    creation_date = models.DateTimeField(auto_now=True, verbose_name="Дата создания")
    last_modified_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата последнего изменения')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='Автор')

    def __str__(self):
        return f"{self.name} ({self.category})"

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('pk',)
        permissions = [
            (
                'set_is_published_product',
                'Can publish Продукт'
            )
        ]


class Contacts(models.Model):
    country = models.CharField(max_length=100, verbose_name='Страна')
    tin = models.CharField(max_length=100, verbose_name='ИНН')
    address = models.CharField(max_length=300, verbose_name='Адрес')

    def __str__(self):
        return f"{self.country}, {self.address}. ИНН: {self.tin}"

    class Meta:
        verbose_name = 'Контактные данные'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    number = models.IntegerField(verbose_name='Номер')
    name = models.CharField(max_length=150, verbose_name='Название')
    is_current_version = models.BooleanField(default=True, verbose_name='Текущая версия')

    def __str__(self):
        return f"{self.name}({self.product})"

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'

