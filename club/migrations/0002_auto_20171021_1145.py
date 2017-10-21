# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-21 08:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsrecord',
            options={'ordering': ['-updated_at', '-created_at']},
        ),
        migrations.AlterField(
            model_name='newsrecord',
            name='description',
            field=models.TextField(verbose_name='Сообщение'),
        ),
        migrations.AlterField(
            model_name='newsrecord',
            name='figure',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/%Y/%m/%d', verbose_name='Картинка'),
        ),
    ]
