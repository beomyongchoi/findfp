# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-27 02:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('subscription_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
