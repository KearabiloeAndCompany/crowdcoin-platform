# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-21 16:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0059_airtimedeposittransaction_sim_card'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airtimedeposittransaction',
            name='created',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
