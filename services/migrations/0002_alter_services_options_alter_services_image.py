# Generated by Django 4.1.2 on 2022-11-01 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='services',
            options={'ordering': ['-created'], 'verbose_name': 'Servicio'},
        ),
        migrations.AlterField(
            model_name='services',
            name='image',
            field=models.ImageField(upload_to='services', verbose_name='Imagen'),
        ),
    ]
