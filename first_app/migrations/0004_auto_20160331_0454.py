# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-31 04:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_commentform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentform',
            name='comment',
            field=models.CharField(max_length=20),
        ),
    ]
