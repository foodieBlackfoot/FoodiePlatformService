# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-27 00:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CookManagement', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meal',
            old_name='Logo',
            new_name='Image',
        ),
    ]
