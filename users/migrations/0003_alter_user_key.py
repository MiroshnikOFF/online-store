# Generated by Django 4.2.5 on 2023-09-29 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='key',
            field=models.IntegerField(blank=True, null=True, verbose_name='Ключ для верификации почты'),
        ),
    ]
