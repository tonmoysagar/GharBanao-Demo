# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-17 01:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designerPic', '0003_designers_designerid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designers',
            name='designerID',
            field=models.CharField(default='xxx@gmail.com', max_length=300),
        ),
    ]