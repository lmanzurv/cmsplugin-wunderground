# -*- coding: utf-8 -*-
from django.conf.urls import *  # NOQA
from .views import *

urlpatterns = [
    url(r'^current-temperature/(?P<plugin>[0-9]+)/$', current_temperature, name='current_temperature'),
]
