# Generated by Django 2.2.1 on 2020-10-06 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='nombres')),
                ('apellido', models.CharField(max_length=50, verbose_name='apellidos')),
                ('direccion', models.CharField(default='', max_length=100, verbose_name='direccion')),
                ('telefono', models.CharField(default=0, max_length=8, verbose_name='telefono')),
            ],
        ),
    ]