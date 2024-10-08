# Generated by Django 5.0.7 on 2024-08-06 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0008_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='title')),
                ('category', models.CharField(max_length=256)),
                ('image', models.ImageField(upload_to=None, verbose_name='image')),
            ],
        ),
    ]
