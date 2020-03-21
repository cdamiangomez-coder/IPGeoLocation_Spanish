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

from datetime import datetime
import os
from termcolor import colored
from sys import platform as _platform


if _platform == 'win32':
    import colorama
    colorama.init()

def Red(value):
        return colored(value, 'red', attrs=['bold'])

def Green(value):
    return colored(value, 'green', attrs=['bold'])


class Logger:

    def __init__(self, nolog=False, verbose=False):
        self.NoLog = nolog
        self.Verbose = verbose


    def WriteLog(self, messagetype, message):
        filename = '{}.log'.format(datetime.strftime(datetime.now(), "%Y%m%d"))
        path = os.path.join('.', 'logs', filename)
        with open(path, 'a') as logFile:
            logFile.write('[{}] {} - {}\n'.format(messagetype, datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S"), message))


    def PrintError(self, message):
        """Mensaje de error de impresión / registro"""
        if not self.NoLog:
            self.WriteLog('ERROR', message)

        print('[{}] {}'.format(Red('ERROR'), message))


    def PrintResult(self, title, value):
        """Imprimir resultado a terminal"""
        print('{}: {}'.format(title, Green(value)))


    def Print(self, message):
        """Mensaje de información de impresión / registro"""
        if not self.NoLog:
            self.WriteLog('INFO', message)

        if self.Verbose:
            print('[{}] {}'.format(Green('**'), message))


    def PrintIPGeoLocation(self, ipGeoLocation):
        """Imprimir información de geolocalización IP a la terminal"""
        self.PrintResult('\nObjetivo', ipGeoLocation.Query)
        self.PrintResult('IP', ipGeoLocation.IP)
        self.PrintResult('ASN', ipGeoLocation.ASN)
        self.PrintResult('Ciudad', ipGeoLocation.City)
        self.PrintResult('País', ipGeoLocation.Country)
        self.PrintResult('Código País', ipGeoLocation.CountryCode)
        self.PrintResult('ISP', ipGeoLocation.ISP)
        self.PrintResult('Latitud', str(ipGeoLocation.Latitude))
        self.PrintResult('Longitud', str(ipGeoLocation.Longtitude))
        self.PrintResult('Organización', ipGeoLocation.Organization)
        self.PrintResult('Código Región', ipGeoLocation.Region)
        self.PrintResult('Nombre Región', ipGeoLocation.RegionName)
        self.PrintResult('Zona Horaria', ipGeoLocation.Timezone)
        self.PrintResult('Código Postal', ipGeoLocation.Zip)
        self.PrintResult('Google Maps', ipGeoLocation.GoogleMapsLink)
        print()
        #.encode('cp737', errors='replace').decode('cp737')
