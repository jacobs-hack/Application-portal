# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-07 17:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumni',
            name='resetExistingEmailPassword',
            field=models.BooleanField(default=False, help_text='Reset password to existing email address'),
        ),
    ]
