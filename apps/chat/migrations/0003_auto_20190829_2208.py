# Generated by Django 2.2.4 on 2019-08-30 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_pytrigger'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pytrigger',
            name='name',
            field=models.CharField(max_length=300, verbose_name='Name'),
        ),
    ]