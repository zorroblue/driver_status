# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-15 14:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cab', '0002_driver_usesapp'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='password',
            field=models.CharField(default='pass', max_length=50),
            preserve_default=False,
        ),
    ]
