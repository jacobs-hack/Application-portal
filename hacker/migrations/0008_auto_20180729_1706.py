# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-29 17:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hacker', '0007_auto_20180722_1542'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dataretentionaccept',
            name='hacker',
        ),
        migrations.AddField(
            model_name='hacker',
            name='jacobsHackTerms',
            field=models.BooleanField(default=True, help_text="I have read and agree to the <a href='/terms/' target='_blank'>JacobsHack Terms and Conditions</a>, including the privacy policy. "),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hacker',
            name='mlhCodeOfConduct',
            field=models.BooleanField(default=True, help_text="I will at all times abide by and conform to the Major League Hacking <a href='https://mlh.io/code-of-conduct'>Code of Conduct</a> while at the event. "),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hacker',
            name='mlhContestTerms',
            field=models.BooleanField(default=True, help_text="I agree to the terms of both the <a href='https://github.com/MLH/mlh-policies/tree/master/prize-terms-and-conditions'>MLH Contest Terms and Conditions</a> and the <a href='https://mlh.io/privacy' target='_blank'>MLH Privacy Policy</a>. "),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hacker',
            name='mlhEmailConsent',
            field=models.BooleanField(default=False, help_text='Yes, I would like to receive informational e-mails and occasional messages about hackathons from MLH as per the MLH Privacy Policy above. '),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='DataRetentionAccept',
        ),
    ]
