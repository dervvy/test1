# Generated by Django 4.2.8 on 2024-04-04 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitecatalog', '0005_product_side_effects_product_country_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Side_effects',
            new_name='side_effects',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='composition',
            new_name='structure',
        ),
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='method_of_application',
        ),
        migrations.AddField(
            model_name='product',
            name='article',
            field=models.TextField(blank=True, verbose_name='Артикул'),
        ),
        migrations.AddField(
            model_name='product',
            name='expiration_date',
            field=models.TextField(blank=True, verbose_name='Срок годности'),
        ),
        migrations.AddField(
            model_name='product',
            name='overdose',
            field=models.TextField(blank=True, verbose_name='Передозировка'),
        ),
        migrations.AddField(
            model_name='product',
            name='reception',
            field=models.TextField(blank=True, verbose_name='Как принимать, курс приема и дозировка'),
        ),
        migrations.AddField(
            model_name='product',
            name='special_instructions',
            field=models.TextField(blank=True, verbose_name='Специальные указания'),
        ),
        migrations.AddField(
            model_name='product',
            name='storage_conditions',
            field=models.TextField(blank=True, verbose_name='Условия хранения'),
        ),
        migrations.AddField(
            model_name='product',
            name='сonditions',
            field=models.TextField(blank=True, verbose_name='Условия отпуска из аптек'),
        ),
    ]