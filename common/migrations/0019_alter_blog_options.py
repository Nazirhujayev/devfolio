# Generated by Django 5.0.7 on 2024-08-08 05:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0018_contact_us'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-id']},
        ),
    ]
