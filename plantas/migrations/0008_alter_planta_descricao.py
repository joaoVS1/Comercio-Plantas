# Generated by Django 4.1 on 2022-08-29 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plantas', '0007_planta_descricao_alter_planta_imageurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planta',
            name='descricao',
            field=models.TextField(default='', max_length=500),
        ),
    ]
