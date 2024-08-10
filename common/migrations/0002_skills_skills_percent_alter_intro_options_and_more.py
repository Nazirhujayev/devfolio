# Generated by Django 5.0.7 on 2024-08-04 17:14

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Skills_percent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percentage', models.IntegerField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='intro',
            options={'verbose_name': 'intro', 'verbose_name_plural': 'intro'},
        ),
        migrations.AlterModelTable(
            name='intro',
            table='intro',
        ),
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('profile', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('content', ckeditor.fields.RichTextField(verbose_name='content')),
                ('skills', models.ManyToManyField(related_name='about', to='common.skills', verbose_name='skills')),
            ],
            options={
                'verbose_name': 'about',
                'verbose_name_plural': 'about',
                'db_table': 'about',
            },
        ),
        migrations.AddField(
            model_name='skills',
            name='language',
            field=models.ManyToManyField(to='common.skills_percent', verbose_name='percent'),
        ),
    ]
