# Generated by Django 4.2.4 on 2023-09-25 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_rename_county_contacts_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='creation_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='product',
            name='last_modified_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата последнего изменения'),
        ),
    ]
