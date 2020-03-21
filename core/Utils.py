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

import webbrowser, ipaddress, socket
from sys import platform as _platform
from subprocess import call
from urllib import request
from core import MyExceptions
from core.Logger import Logger

class Utils:

    def __init__(self, nolog=False, verbose=False):
        self.Logger = Logger(nolog, verbose)


    def openLocationInGoogleMaps(self, ipGeolObj):
        """Abra la geolocalización IP en Google Maps con el navegador predeterminado"""
        if type(ipGeolObj.Longtitude) == float and type(ipGeolObj.Latitude) == float:
            self.Logger.Print('Abrir Geolocalización en el navegador..')

            if _platform == 'cygwin':
                call(['cygstart', ipGeolObj.GoogleMapsLink])

            elif _platform == 'win32' or _platform == 'linux' or _platform == 'linux2':
                webbrowser.open(ipGeolObj.GoogleMapsLink)

            else:
                self.Logger.PrintError('-g la opción no está disponible en su plataforma.')


    def hostnameToIP(self, hostname):
        """Resolver nombre de host a la dirección IP"""
        try:
            return socket.gethostbyname(hostname)
        except:
            return False


    def isValidIPAddress(self, ip):
        """Compruebe si ip es una dirección IPv4 / IPv6 válida"""
        try:
            ipaddress.ip_address(ip)
            return True
        except:
            return False


    def checkProxyConn(self, url, proxy):
        """Verificar la conectividad del proxy"""
        check = True
        self.Logger.Print('Probando conectividad del Proxy {}...'.format(proxy))

        try:
            req = request.Request(url)
            req.set_proxy(proxy, 'http')
            request.urlopen(req)
        except:
            check = False

        if check == True:
            self.Logger.Print('Se puede acceder al servidor proxy.')
        else:
            raise MyExceptions.ProxyServerNotReachableError()
