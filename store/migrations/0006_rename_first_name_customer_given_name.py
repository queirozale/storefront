# Generated by Django 3.2.7 on 2021-09-18 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_add_zip_to_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='first_name',
            new_name='given_name',
        ),
    ]
