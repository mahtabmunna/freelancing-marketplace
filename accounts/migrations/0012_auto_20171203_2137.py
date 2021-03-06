# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-03 15:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20171125_0824'),
    ]

    operations = [
        migrations.AddField(
            model_name='profileemp',
            name='about',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='profileemp',
            name='address1',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='profileemp',
            name='address2',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='profileemp',
            name='city',
            field=models.CharField(default='Chittagong', max_length=200),
        ),
        migrations.AddField(
            model_name='profileemp',
            name='company',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='profileemp',
            name='country',
            field=models.CharField(default='Bangladesh', max_length=200),
        ),
        migrations.AddField(
            model_name='profileemp',
            name='website',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='profilefree',
            name='about',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='profilefree',
            name='address1',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='profilefree',
            name='address2',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='profilefree',
            name='city',
            field=models.CharField(default='Chittagong', max_length=200),
        ),
        migrations.AddField(
            model_name='profilefree',
            name='company',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='profilefree',
            name='country',
            field=models.CharField(default='Bangladesh', max_length=200),
        ),
        migrations.AddField(
            model_name='profilefree',
            name='website',
            field=models.URLField(null=True),
        ),
    ]
