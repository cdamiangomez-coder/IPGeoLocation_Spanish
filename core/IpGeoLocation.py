#!/usr/bin/env python3
# encoding: UTF-8

"""
    Este archivo es parte de IPGeoLocation tool.
    Copyright (C) 2015-2016 @maldevel
    https://github.com/maldevel/IPGeoLocation

    IPGeoLocation - Retrieve IP Geolocation information
    Powered by http://ip-api.com

    Este programa es software libre: puede redistribuirlo y / o modificarlo
    bajo los términos de la Licencia Pública General GNU publicada por
    Free Software Foundation, ya sea la versión 3 de la Licencia, o
    (a su elección) cualquier versión posterior.

    Este programa se distribuye con la esperanza de que sea útil,
    pero SIN NINGUNA GARANTÍA; sin siquiera la garantía implícita de
    COMERCIABILIDAD o APTITUD PARA UN PROPÓSITO EN PARTICULAR. Ver el
    Licencia pública general de GNU para más detalles.

    Debería haber recibido una copia de la Licencia Pública General de GNU
    junto con este programa. Si no, vea <http://www.gnu.org/licenses/>.

    Para obtener más información, consulte el archivo 'LICENCIA' para obtener permiso de copia.
"""

__author__ = 'maldevel'
__español__ = 'cdamiangomez'


class IpGeoLocation:
    """Representa un objeto de información de geolocalización IP"""

    def __init__(self, query, jsonData = None):
        self.Query = query
        self.ASN = '-'
        self.City = '-'
        self.Country = '-'
        self.CountryCode = '-'
        self.ISP = '-'
        self.Latitude = 0.0
        self.Longtitude = 0.0
        self.Organization = '-'
        self.IP = '0.0.0.0'
        self.Region = '-'
        self.RegionName = '-'
        self.Status = '-'
        self.Timezone = '-'
        self.Zip = '-'
        self.GoogleMapsLink = ''

        if jsonData != None:
            if type(jsonData) is dict:
                if 'as' in jsonData:
                    self.ASN = jsonData['as']

                if 'city' in jsonData:
                    self.City = jsonData['city']

                if 'country' in jsonData:
                    self.Country = jsonData['country']

                if 'countryCode' in jsonData:
                    self.CountryCode = jsonData['countryCode']

                if 'isp' in jsonData:
                    self.ISP = jsonData['isp']

                if 'lat' in jsonData:
                    self.Latitude = jsonData['lat']

                if 'lon' in jsonData:
                    self.Longtitude = jsonData['lon']

                if 'org' in jsonData:
                    self.Organization = jsonData['org']

                if 'query' in jsonData:
                    self.IP = jsonData['query']

                if 'region' in jsonData:
                    self.Region = jsonData['region']

                if 'regionName' in jsonData:
                    self.RegionName = jsonData['regionName']

                if 'status' in jsonData:
                    self.Status = jsonData['status']

                if 'timezone' in jsonData:
                    self.Timezone = jsonData['timezone']

                if 'zip' in jsonData:
                    self.Zip = jsonData['zip']

                if type(self.Latitude) == float and type(self.Longtitude) == float:
                    self.GoogleMapsLink = 'http://www.google.com/maps/place/{0},{1}/@{0},{1},16z'.format(self.Latitude, self.Longtitude)


    def ToDict(self):
        #self.__dict__.
        return {'Objetivo':self.Query, 'IP':self.IP, 'ASN':self.ASN, 'Ciudad':self.City,
                    'País':self.Country, 'Código País':self.CountryCode, 'ISP':self.ISP,
                    'Latitud':str(self.Latitude), 'Longitud':str(self.Longtitude),
                    'Organización':self.Organization, 'Region':self.Region,
                    'Nombre Region':self.RegionName, 'Zona Horaria':self.Timezone,
                    'Código Postal':self.Zip, 'Google Maps':self.GoogleMapsLink
                }
