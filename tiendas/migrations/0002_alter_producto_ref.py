# Generated by Django 5.0.2 on 2024-05-31 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiendas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='ref',
            field=models.CharField(blank=True, max_length=16, null=True, verbose_name='Referencia'),
        ),
    ]
