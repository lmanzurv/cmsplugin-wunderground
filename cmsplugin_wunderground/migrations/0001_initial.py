# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentTemperature',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('zip_code', models.CharField(max_length=12, null=True, verbose_name='Zip Code', blank=True)),
                ('coordinates', models.CharField(max_length=50, null=True, verbose_name='Latitude & Longitude Coordinates', blank=True)),
            ],
            options={
                'verbose_name': 'Current Temperature',
                'verbose_name_plural': 'Current Temperatures',
            },
            bases=('cms.cmsplugin',),
        ),
    ]
