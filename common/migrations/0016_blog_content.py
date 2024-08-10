# Generated by Django 5.0.7 on 2024-08-07 09:55

import ckeditor.fields
import django.utils.timezone
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0015_alter_blog_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='content',
            field=ckeditor.fields.RichTextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]