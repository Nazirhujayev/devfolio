# Generated by Django 5.0.7 on 2024-08-04 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_alter_about_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skills_percent',
            old_name='percentage',
            new_name='number',
        ),
    ]
