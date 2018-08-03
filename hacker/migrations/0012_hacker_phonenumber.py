# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-03 05:15
from __future__ import unicode_literals

from django.db import migrations
import hacker.fields


class Migration(migrations.Migration):

    dependencies = [
        ('hacker', '0011_hacker_countryofresidence'),
    ]

    operations = [
        migrations.AddField(
            model_name='hacker',
            name='phoneNumber',
            field=hacker.fields.PhoneField(default='+494212000000', max_length=128),
            preserve_default=False,
        ),
    ]