# Generated by Django 3.1.1 on 2021-06-17 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='post_user',
        ),
    ]
