# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 20:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=100)),
                ('travelstartdate', models.DateTimeField(default=datetime.datetime(2017, 7, 27, 13, 6, 7, 17000))),
                ('travelenddate', models.DateTimeField(default=datetime.datetime(2017, 7, 27, 13, 6, 7, 18000))),
                ('description', models.CharField(max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('joiners', models.ManyToManyField(related_name='joiners', to='login_app.User')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login_app.User')),
            ],
        ),
    ]
