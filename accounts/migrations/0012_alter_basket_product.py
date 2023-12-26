# Generated by Django 4.2.1 on 2023-07-07 22:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_category_detail'),
        ('accounts', '0011_basket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.variants'),
        ),
    ]