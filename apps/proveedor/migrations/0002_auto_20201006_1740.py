# Generated by Django 2.2.1 on 2020-10-06 23:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proveedor', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='proveedor',
            options={'ordering': ['-id'], 'verbose_name': 'Proveedor', 'verbose_name_plural': 'Proveedores'},
        ),
    ]
