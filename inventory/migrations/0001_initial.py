# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-19 16:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductTestData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(max_length=200)),
                ('method', models.CharField(max_length=200)),
                ('unit', models.CharField(max_length=200)),
                ('mins', models.CharField(max_length=200)),
                ('maxs', models.CharField(max_length=200)),
                ('typical', models.CharField(max_length=2)),
                ('product_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.ProductName')),
            ],
        ),
        migrations.CreateModel(
            name='ProductTestList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(max_length=200)),
                ('unit', models.CharField(max_length=200)),
                ('mins', models.CharField(max_length=200)),
                ('maxs', models.CharField(max_length=200)),
                ('typical', models.CharField(max_length=200)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('product_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.ProductName')),
            ],
        ),
        migrations.CreateModel(
            name='TestName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(max_length=200, unique=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='producttestlist',
            name='test_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.TestName'),
        ),
    ]