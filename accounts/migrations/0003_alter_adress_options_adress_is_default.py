# Generated by Django 4.2.1 on 2023-06-26 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='adress',
            options={'verbose_name_plural': 'Adress'},
        ),
        migrations.AddField(
            model_name='adress',
            name='is_default',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
