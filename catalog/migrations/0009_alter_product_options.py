# Generated by Django 4.2.6 on 2023-10-19 22:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_product_is_published'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('pk',), 'permissions': [('set_is_published_product', 'Can publish Продукт')], 'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
    ]