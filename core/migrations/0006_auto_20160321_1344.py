# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-21 17:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20160321_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.FileField(default=b'http://www.istockphoto.com/static/images/banshee/avatar-placeholder.svg', upload_to=b'user-profile-pic'),
        ),
    ]
