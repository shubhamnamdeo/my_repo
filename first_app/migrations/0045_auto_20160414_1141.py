# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-14 06:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0044_auto_20160414_1139'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Consultant',
        ),
        migrations.AlterField(
            model_name='art',
            name='dates',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 14, 6, 11, 6, 104253, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='commentform',
            name='dates',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 14, 6, 11, 6, 103215, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='note',
            name='dates',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 14, 6, 11, 6, 103748, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='word',
            name='dates',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 14, 6, 11, 6, 104713, tzinfo=utc)),
        ),
    ]
