# Generated by Django 3.2.4 on 2021-06-05 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_remove_product_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='product',
            new_name='insertProduct',
        ),
    ]
