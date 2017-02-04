# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-03 17:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='trialapp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('image', models.TextField(blank=True, max_length=10000, null=True)),
                ('auther', models.TextField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, max_length=250000, null=True)),
            ],
        ),
    ]