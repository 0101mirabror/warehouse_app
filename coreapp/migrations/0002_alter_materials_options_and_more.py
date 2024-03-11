# Generated by Django 5.0.3 on 2024-03-09 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='materials',
            options={'verbose_name_plural': 'Xomashyolar'},
        ),
        migrations.AlterModelOptions(
            name='productmaterials',
            options={'verbose_name_plural': 'Mahsulot-Xomashyolar'},
        ),
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name_plural': 'Mahsulotlar'},
        ),
        migrations.AlterModelOptions(
            name='warehouses',
            options={'verbose_name_plural': 'Omborxonalar'},
        ),
        migrations.AlterField(
            model_name='productmaterials',
            name='quantity',
            field=models.FloatField(),
        ),
    ]
