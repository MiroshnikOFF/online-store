# Generated by Django 4.2.5 on 2023-09-29 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='key',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='Ключ для верификации почты'),
        ),
    ]
