# Generated by Django 4.1 on 2022-08-27 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Planta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('nome_cientifico', models.CharField(max_length=50)),
                ('origem', models.CharField(max_length=50)),
            ],
        ),
    ]