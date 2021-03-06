# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-22 15:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import hacker.models
import hacker.validators


class Migration(migrations.Migration):

    dependencies = [
        ('hacker', '0006_merge_20180704_2158'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataRetentionAccept',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mlhContestTerms', models.BooleanField()),
                ('mlhCodeOfConduct', models.BooleanField()),
                ('GDPRClause', models.BooleanField()),
                ('hacker', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='privacy_policy', to='hacker.Hacker')),
            ],
        ),
        migrations.AlterField(
            model_name='cv',
            name='cv',
            field=models.FileField(blank=True, help_text='Your CV (optional)', null=True, upload_to=hacker.models.upload_to, validators=[hacker.validators.FileExtensionValidator(['.pdf'])]),
        ),
    ]
