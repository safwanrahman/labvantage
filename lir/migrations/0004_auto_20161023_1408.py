# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-23 08:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lir', '0003_auto_20161022_1319'),
    ]

    operations = [
        migrations.AddField(
            model_name='productinfo',
            name='lab_request_form',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='lir.LabRequestForm'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productinfo',
            name='batch_number',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='productinfo',
            name='batch_size',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='productinfo',
            name='blending_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='productinfo',
            name='date_tested',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='productinfo',
            name='product_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.ProductName'),
        ),
        migrations.AlterField(
            model_name='productinfo',
            name='sample_number',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='productinfo',
            name='serial_number',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='productinfo',
            name='tank_number',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='productinfo',
            name='test_type',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='productinfo',
            name='time_in_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='productinfo',
            name='time_out_date',
            field=models.DateTimeField(null=True),
        ),
    ]