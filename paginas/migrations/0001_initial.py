# Generated by Django 5.0.2 on 2024-05-12 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Título')),
                ('content', models.TextField(verbose_name='Descripción')),
                ('slug', models.CharField(max_length=150, unique=True, verbose_name='URL sencilla')),
                ('visible', models.BooleanField(verbose_name='Visible')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creación')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Última actualización')),
            ],
        ),
    ]
