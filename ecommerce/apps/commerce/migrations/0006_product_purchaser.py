# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-28 16:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0002_auto_20170727_2053'),
        ('commerce', '0005_product_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='purchaser',
            field=models.ManyToManyField(related_name='purchaser', to='login_app.User'),
        ),
    ]
