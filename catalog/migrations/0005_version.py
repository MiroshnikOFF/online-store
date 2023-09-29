# Generated by Django 4.2.4 on 2023-09-25 21:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_product_creation_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(max_length=150, verbose_name='Номер')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('is_current_version', models.BooleanField(default=True, verbose_name='Текущая версия')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Версия',
                'verbose_name_plural': 'Версии',
            },
        ),
    ]