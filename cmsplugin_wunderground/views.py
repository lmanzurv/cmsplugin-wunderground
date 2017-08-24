# -*- coding: utf-8 -*-
from .models import CurrentTemperatureCache, CurrentTemperature
from django.http import JsonResponse, HttpResponseNotAllowed
from django.contrib.sites.models import Site
from django.utils import timezone
from cmsplugin_site_settings.models import SiteProperty
import urllib2, json, warnings, datetime

def current_temperature(request, plugin):
    if request.method == 'GET':
        error = None
        site = Site.objects.get_current()

        try:
            test = SiteProperty.objects.values('value').get(settings__site=site, name='WUNDERGROUND_TEST').get('value')
        except:
            error = 'Please define the WUNDERGROUND_TEST property for the current site'
            warnings.warn(error)

        if not error:
            try:
                kwargs = dict(plugin_id=plugin)
                if test != 'True':
                    kwargs['expiration_date__gte'] = timezone.now()
                temp = json.loads(CurrentTemperatureCache.objects.values('value').get(**kwargs).get('value'))
            except:
                try:
                    key = SiteProperty.objects.values('value').get(settings__site=site, name='WUNDERGROUND_KEY').get('value')
                except:
                    error = 'Please define the WUNDERGROUND_KEY property for the current site'
                    warnings.warn(error)

                if not error:
                    try:
                        temp_plugin = CurrentTemperature.objects.get(id=plugin)
                        location = temp_plugin.zip_code if temp_plugin.zip_code else temp_plugin.coordinates
                        conn = urllib2.urlopen('https://api.wunderground.com/api/%s/geolookup/conditions/q/%s.json' % (key, location))
                        response = json.loads(conn.read())
                        conn.close()

                        if 'reponse' in response and 'error' in response['response']:
                            error = response['response']['error']['description']
                        else:
                            temp = {
                                'location': response['location']['city'],
                                'temp_c': response['current_observation']['temp_c'],
                                'temp_f': response['current_observation']['temp_f']
                            }

                            CurrentTemperatureCache.objects.update_or_create(plugin=temp_plugin,
                                defaults={'plugin': temp_plugin, 'value': json.dumps(temp), 'expiration_date': timezone.now() + datetime.timedelta(hours=1)})
                    except:
                        # Load the old registry in case we cannot fetch the latest
                        temp = json.loads(CurrentTemperatureCache.objects.values('value').get(dict(plugin_id=plugin)).get('value'))
        if error:
            resp = {'error': error}
        else:
            resp = {'temp': temp}

        return JsonResponse(resp, status=200)
    else:
        return HttpResponseNotAllowed(['GET'])
