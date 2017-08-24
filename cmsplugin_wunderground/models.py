# -*- coding: utf-8 -*-
from django.db import models
from cms.models.pluginmodel import CMSPlugin
from aldryn_bootstrap3.model_fields import Icon
from django.utils.translation import ugettext_lazy as _

class CurrentTemperature(CMSPlugin):
    zip_code = models.CharField(max_length=12, verbose_name=_('Zip Code'), null=True, blank=True)
    coordinates = models.CharField(max_length=50, verbose_name=_('Latitude & Longitude Coordinates'), null=True, blank=True)
    icon = Icon()

    class Meta:
        verbose_name = _('Current Temperature')
        verbose_name_plural = _('Current Temperatures')

    def __unicode__(self):
        return self.zip_code if self.zip_code else self.coordinates

class CurrentTemperatureCache(models.Model):
    plugin = models.ForeignKey(CurrentTemperature, related_name='cache_plugin')
    value = models.TextField(verbose_name=_('API response'))
    expiration_date = models.DateTimeField(verbose_name=_('API response expiration'))

    def _unicode__(self):
        return ''
