# Generated by Django 4.1.1 on 2022-09-28 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20220927_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.BigAutoField(
                auto_created=True, primary_key=True,
                serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.BigAutoField(
                auto_created=True, primary_key=True,
                serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='review',
            name='id',
            field=models.BigAutoField(
                auto_created=True, primary_key=True,
                serialize=False, verbose_name='ID'),
        ),
    ]
