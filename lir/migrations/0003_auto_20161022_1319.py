# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-22 07:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lir', '0002_auto_20161022_1123'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Lir',
            new_name='LabRequestForm',
        ),
    ]