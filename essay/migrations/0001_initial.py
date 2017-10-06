# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-05 20:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Essay_Question',
            fields=[
                ('question_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='quiz.Question')),
            ],
            options={
                'verbose_name': 'Essay style question',
                'verbose_name_plural': 'Essay style questions',
            },
            bases=('quiz.question',),
        ),
    ]
