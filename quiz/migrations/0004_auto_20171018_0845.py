# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-18 05:45
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_quiz_subcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='figure',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/%Y/%m/%d', verbose_name='Рисунок'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='pass_mark',
            field=models.SmallIntegerField(blank=True, default=0, help_text='Процент правильных ответов для прохождения теста', validators=[django.core.validators.MaxValueValidator(100)], verbose_name='Порог успеха'),
        ),
    ]
