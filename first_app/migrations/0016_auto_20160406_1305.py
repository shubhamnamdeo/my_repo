# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-06 07:35
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0015_auto_20160406_1245'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docfile', models.FileField(upload_to='documents/%Y/%m/%d')),
            ],
        ),
        migrations.AlterField(
            model_name='artform',
            name='dates',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 6, 7, 35, 36, 349250, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='commentform',
            name='dates',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 6, 7, 35, 36, 348793, tzinfo=utc)),
        ),
    ]
