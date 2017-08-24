# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _

class CurrentTemperatureForm(forms.ModelForm):
    def clean(self):
        zip_code = self.cleaned_data.get('zip_code')
        coordinates = self.cleaned_data.get('coordinates')

        if not zip_code and not coordinates:
            raise forms.ValidationError(_('Either zip code or coordinates must be defined'))

        if zip_code and coordinates:
            raise forms.ValidationError(_('Either zip code or coordinates must be defined, not both'))

    def clean_coordinates(self):
        data = self.cleaned_data.get('coordinates')
        data = ''.join(data.split())
        return data
