# -*- coding: utf-8 -*-
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from .models import CurrentTemperature
from .forms import CurrentTemperatureForm

class CurrentTemperaturePlugin(CMSPluginBase):
    model = CurrentTemperature
    name = _('Curren Temperature')
    module = _('Weather')
    render_template = 'current_temperature.html'
    change_form_template = 'admin/current_temperature.html'
    form = CurrentTemperatureForm

    def render(self, context, instance, placeholder):
        context = super(CurrentTemperaturePlugin, self).render(context, instance, placeholder)
        return context

plugin_pool.register_plugin(CurrentTemperaturePlugin)
