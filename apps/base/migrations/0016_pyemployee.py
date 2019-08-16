# Generated by Django 2.2.4 on 2019-08-16 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_auto_20190816_2050'),
    ]

    operations = [
        migrations.CreateModel(
            name='PyEmployee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='Nombre')),
                ('name2', models.CharField(max_length=80, verbose_name='Segundo Nombre')),
                ('first_name', models.CharField(max_length=80, verbose_name='Apellido Paterno')),
                ('last_name', models.CharField(max_length=80, verbose_name='Apellido Materno')),
                ('phone', models.CharField(blank=True, max_length=20, verbose_name='Teléfono')),
                ('email', models.CharField(blank=True, max_length=40, verbose_name='Correo')),
            ],
        ),
    ]
