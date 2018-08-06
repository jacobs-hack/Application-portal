# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-06 00:22
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import hacker.models


class Migration(migrations.Migration):

    dependencies = [
        ('hacker', '0021_auto_20180805_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='cv',
            field=models.FileField(blank=True, help_text='Optionally upload your CV here. Uploading your CV <b>does not</b> constitute consent to transmitting the CV to our sponsors. We will contact you regarding this seperatly. ', null=True, upload_to=hacker.models.upload_to, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])]),
        ),
    ]