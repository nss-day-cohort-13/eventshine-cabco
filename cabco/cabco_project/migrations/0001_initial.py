# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-26 15:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('begin_date_time', models.DateTimeField()),
                ('end_date_time', models.DateTimeField()),
                ('atendee_limit', models.IntegerField(default=0)),
                ('event_price', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venue_name', models.CharField(max_length=200)),
                ('seating_capacity', models.IntegerField(default=0)),
            ],
        ),
    ]