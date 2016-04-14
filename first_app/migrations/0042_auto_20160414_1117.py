# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-14 05:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0041_auto_20160414_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='art',
            name='dates',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 14, 5, 47, 44, 143103, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='commentform',
            name='dates',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 14, 5, 47, 44, 142064, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='consultant',
            name='dates',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 14, 5, 47, 44, 144351, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='consultant',
            name='log_user',
            field=models.CharField(default='676', max_length=30),
        ),
        migrations.AlterField(
            model_name='note',
            name='dates',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 14, 5, 47, 44, 142586, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='word',
            name='dates',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 14, 5, 47, 44, 143604, tzinfo=utc)),
        ),
    ]
