# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2016-12-29 13:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perpus', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='pic_book',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
