# Generated by Django 4.2.1 on 2023-06-03 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SliderImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('path', models.ImageField(upload_to='SliderImages')),
            ],
            options={
                'verbose_name_plural': 'SliderImages',
            },
        ),
    ]
