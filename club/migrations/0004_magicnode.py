# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-05 18:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0003_examevent'),
    ]

    operations = [
        migrations.CreateModel(
            name='MagicNode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sib_order', models.PositiveIntegerField()),
                ('desc', models.CharField(max_length=255)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children_set', to='club.MagicNode')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
