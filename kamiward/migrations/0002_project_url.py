# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-09-05 13:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kamiward', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='url',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]