# Generated by Django 4.2.8 on 2024-02-04 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitecatalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('name',), 'verbose_name': 'Товары', 'verbose_name_plural': 'Товары'},
        ),
    ]
