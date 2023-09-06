from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    created_at = models.CharField(max_length=100, **NULLABLE)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = "Категории"


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    image = models.ImageField(upload_to='images/', verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена за покупку')
    creation_date = models.DateTimeField(verbose_name="Дата создания")
    last_modified_date = models.DateTimeField(verbose_name='Дата последнего изменения')

    def __str__(self):
        return f"{self.name} ({self.category})"

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
