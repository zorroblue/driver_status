# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-13 19:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('driver_number', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
            ],
        ),
    ]
