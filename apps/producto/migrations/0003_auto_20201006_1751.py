# Generated by Django 2.2.1 on 2020-10-06 23:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0002_auto_20201006_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalleproducto',
            name='fechavencimiento',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de vencimiento'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='tipopresentacion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='producto.TipoPresentacion'),
        ),
    ]
