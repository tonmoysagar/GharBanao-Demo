# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-17 02:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designerPic', '0004_auto_20161217_0654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designers',
            name='designerID',
            field=models.CharField(default='des000', max_length=13),
        ),
    ]
