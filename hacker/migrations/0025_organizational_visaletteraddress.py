# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-27 20:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hacker', '0024_organizational_passportnumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizational',
            name='visaLetterAddress',
            field=models.TextField(blank=True, default='', help_text='Your address (to send you a visa letter)', null=True),
        ),
    ]
