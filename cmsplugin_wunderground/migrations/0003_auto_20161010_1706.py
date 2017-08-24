# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-10 15:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_wunderground', '0002_auto_20160831_0259'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentTemperatureCache',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField(verbose_name='API response')),
                ('expiration_date', models.DateTimeField(verbose_name='API response expiration')),
            ],
        ),
        migrations.AddField(
            model_name='currenttemperaturecache',
            name='plugin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cache_plugin', to='cmsplugin_wunderground.CurrentTemperature'),
        ),
    ]
