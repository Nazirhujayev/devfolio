# Generated by Django 5.0.7 on 2024-08-06 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0014_blogcategory_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='duration',
            field=models.CharField(max_length=256, verbose_name='duration'),
        ),
    ]
