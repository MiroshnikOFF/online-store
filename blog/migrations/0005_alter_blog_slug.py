# Generated by Django 4.2.4 on 2023-09-14 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blog_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(max_length=150, unique=True, verbose_name='slug'),
        ),
    ]