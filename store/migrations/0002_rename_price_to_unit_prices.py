# Generated by Django 3.2.7 on 2021-09-18 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='unit_prices',
        ),
    ]
