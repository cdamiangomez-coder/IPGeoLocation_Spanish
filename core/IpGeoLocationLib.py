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

from core.Utils import Utils
import json, random, os
from core.MyExceptions import *
from core.IpGeoLocation import IpGeoLocation
from time import sleep
from core.FileExporter import FileExporter
from urllib.parse import urlparse
from urllib import request

class IpGeoLocationLib:
    """Recuperar información de geolocalización IP de http://ip-api.com"""

    def __init__(self, target, logger, noprint=False, nolog=False, verbose=False):
        self.URL = 'http://ip-api.com'
        self.RequestURL = self.URL + '/json/{}'
        self.BOLD = '\033[1m'
        self.Proxy = None
        self.UserAgentFile = None
        self.UserAgents = None
        self.Proxies = None
        self.TargetsFile = None
        self.ProxiesFile = None
        self.Targets = None
        self.NoPrint = noprint
        self.Target = target
        self.Logger = logger
        self.Utils = Utils(nolog, verbose)

    def GetInfo(self, userAgent, targetsFile=None,
                userAgentFile=None, proxy=False, proxiesFile=None,
                exportToCSVFile=None, exportToXMLFile=None,
                exportToTXTFile=None, googleMaps=False):
        """Recuperar la información"""

        self.UserAgent = userAgent

        try:

            #check proxies file and load it
            if proxiesFile and os.path.isfile(proxiesFile) and os.access(proxiesFile, os.R_OK):
                self.ProxiesFile = proxiesFile
                self.Logger.Print('Cargando Proxies desde archivo {}..'.format(self.ProxiesFile))
                self.__loadProxies()

            #check user-agent strings file and load it
            if userAgentFile and os.path.isfile(userAgentFile) and os.access(userAgentFile, os.R_OK):
                self.UserAgentFile = userAgentFile
                self.Logger.Print('Cargando Agentes-Usuarios desde archivo {}..'.format(self.UserAgentFile))
                self.__loadUserAgents()

            #check targets file and load it
            if targetsFile and os.path.isfile(targetsFile) and os.access(targetsFile, os.R_OK):
                self.TargetsFile = targetsFile
                self.Logger.Print('Cargando destinos desde archivo {}..'.format(self.TargetsFile))
                self.__loadTargets()

            #check if proxy valid and configure connection
            if proxy:
                self.__configureProxy(proxy)


            #retrieve information
            results = None
            if self.TargetsFile:
                results = self.__retrieveGeolocations()

            else:
                results = self.__retrieveGeolocation(self.Target)

            #export information
            if exportToCSVFile and not os.path.exists(exportToCSVFile) and os.access(os.path.dirname(exportToCSVFile), os.W_OK):
                self.__exportResultsToCSV(results, exportToCSVFile)

            if exportToXMLFile and not os.path.exists(exportToXMLFile) and os.access(os.path.dirname(exportToXMLFile), os.W_OK):
                self.__exportResultsToXML(results, exportToXMLFile)

            if exportToTXTFile and not os.path.exists(exportToTXTFile) and os.access(os.path.dirname(exportToTXTFile), os.W_OK):
                self.__exportResultsToTXT(results, exportToTXTFile)

            #open location in Google Maps with default browser
            if googleMaps and type(results) is IpGeoLocation:
                self.Utils.openLocationInGoogleMaps(results)

            return True

        except UserAgentFileEmptyError:
            self.Logger.PrintError("Agentes-Usuarios: archivo vacío!")
        except InvalidTargetError:
            self.Logger.PrintError('Por favor indique Dominio o IP válido!')
        except TargetsFileEmptyError:
            self.Logger.PrintError('El archivo de Destino está vacío!')
        except UserAgentFileNotSpecifiedError:
            self.Logger.PrintError('Usuarios: Los valores o cadenas no han sido provistos!')
        except TargetsFileNotSpecifiedError:
            self.Logger.PrintError('No se ha proporcionado el archivo de objetivos!')
        except ProxyServerNotReachableError:
            self.Logger.PrintError('Servidor proxy no accesible!')
        except ProxiesFileNotSpecifiedError:
            self.Logger.PrintError('No se ha proporcionado el archivo proxy!')
        except ProxiesFileEmptyError:
            self.Logger.PrintError('Proxies file is empty!')
        except InvalidProxyUrlError:
            self.Logger.PrintError('La URL del proxy no es válida!')
        except Exception as error:
            self.Logger.PrintError('Ocurrió un error inesperado {}!'.format(error))

        return False

    def __checkProxyUrl(self, url):
        """Compruebe si la URL del proxy es válida"""
        url_checked = urlparse(url)
        if (url_checked.scheme not in ('http', 'https')) | (url_checked.netloc == ''):
            return False
        return url_checked


    def __configureProxy(self, proxy):
        #proxy = self.__checkProxyUrl(proxy)
        #if not proxy:
        #    raise MyExceptions.InvalidProxyUrlError()

        self.Utils.checkProxyConn(self.URL, proxy.netloc)
        self.Proxy = proxy
        proxyHandler = request.ProxyHandler({'http':proxy.scheme + '://' + proxy.netloc})
        opener = request.build_opener(proxyHandler)
        request.install_opener(opener)
        self.Logger.Print('Proxy ({}) ha sido configurado.'.format(proxy.scheme + '://' + proxy.netloc))


    def __exportResultsToCSV(self, objToExport, csvFile):
        """Exportar resultados a archivo csv"""
        fileExporter = FileExporter()
        self.Logger.Print('Se guardó resultados en {} archivo CSV.'.format(csvFile))
        success = False

        if type(objToExport) is IpGeoLocation:
            success = fileExporter.ExportToCSV(objToExport, csvFile)
        elif type(objToExport) is list:
            success = fileExporter.ExportListToCSV(objToExport, csvFile)

        if not success:
            self.Logger.PrintError('Guardando resultados en {} archivo CSV ha fallado.'.format(csvFile))


    def __exportResultsToXML(self, objToExport, xmlFile):
        """Exportar resultados a archivo xml"""
        fileExporter = FileExporter()
        self.Logger.Print('Se guardó resultados en {} archivo XML.'.format(xmlFile))
        success = False

        if type(objToExport) is IpGeoLocation:
            success = fileExporter.ExportToXML(objToExport, xmlFile)
        elif type(objToExport) is list:
            success = fileExporter.ExportListToXML(objToExport, xmlFile)

        if not success:
            self.Logger.PrintError('Guardando resultados en {} archivo XML ha fallado.'.format(xmlFile))


    def __exportResultsToTXT(self, objToExport, txtFile):
        """Exportar resultados a archivo de texto"""
        fileExporter = FileExporter()
        self.Logger.Print('Se guardó resultados en {} archivo de Texto.'.format(txtFile))
        success = False

        if type(objToExport) is IpGeoLocation:
            success = fileExporter.ExportToTXT(objToExport, txtFile)
        elif type(objToExport) is list:
            success = fileExporter.ExportListToTXT(objToExport, txtFile)

        if not success:
            self.Logger.PrintError('Guardando resultados en {} archivo de Texto ha fallado.'.format(txtFile))


    def __retrieveGeolocations (self):
        """Recupere la geolocalización de IP para cada objetivo en la lista"""
        IpGeoLocObjs = []

        for target in self.Targets:
            IpGeoLocObjs.append(self.__retrieveGeolocation(target))
            if len(self.Targets)>=150:
                sleep(.500) #1/2 sec - ip-api will automatically ban any IP address doing over 150 requests per minute

        return IpGeoLocObjs


    def __retrieveGeolocation(self, target):
        """Recupere la geolocalización de IP para un solo objetivo"""

        if not target:
            query = 'Mi IP'
            target=''

        elif self.Utils.isValidIPAddress(target):
            query = target

        else:
            ip = self.Utils.hostnameToIP(target)#domain?
            if not ip:
                raise InvalidTargetError()

            query = target
            target = ip


        #pick random user-agent string
        if self.UserAgentFile:
            self.__pickRandomUserAgent()


        #pick random proxy connection
        if self.ProxiesFile:
            self.__pickRandomProxy()


        self.Logger.Print('Recuperando Geolocalización de {}...'.format(query))

        req = request.Request(self.RequestURL.format(target), data=None, headers={
          'User-Agent':self.UserAgent
        })

        response = request.urlopen(req)

        if response.code == 200:

            self.Logger.Print('Usuario-Agente usado: {}'.format(self.UserAgent))

            encoding = response.headers.get_content_charset()
            ipGeoLocObj = IpGeoLocation(query, json.loads(response.read().decode(encoding)))

            self.Logger.Print('La información de geolocalización se ha recuperado para {} ({}).'.format(query, ipGeoLocObj.IP))

            if not self.NoPrint:
                self.Logger.PrintIPGeoLocation(ipGeoLocObj)

            return ipGeoLocObj

        return False


    def __loadProxies(self):
        """Cargar proxies del archivo"""
        if not self.ProxiesFile:
            raise ProxiesFileNotSpecifiedError()

        self.Proxies = [line.strip() for line in open(self.ProxiesFile, 'r') if line.strip()]
        self.Logger.Print('{} Proxies cargados.'.format(len(self.Proxies)))

        if len(self.Proxies) == 0:
            raise ProxiesFileEmptyError()


    def __loadUserAgents(self):
        """Cargar cadenas de agente de usuario del archivo"""
        if not self.UserAgentFile:
            raise UserAgentFileNotSpecifiedError()

        self.UserAgents = [line.strip() for line in open(self.UserAgentFile, 'r') if line.strip()]
        self.Logger.Print('{} Cadenas de agente de usuario cargadas.'.format(len(self.UserAgents)))

        if len(self.UserAgents) == 0:
            raise UserAgentFileEmptyError()


    def __loadTargets(self):
        """Cargar objetivos desde el archivo"""
        if not self.TargetsFile:
            raise TargetsFileNotSpecifiedError()

        self.Targets = [line.strip() for line in open(self.TargetsFile, 'r') if line.strip()]
        self.Logger.Print('{} Objetivos cargados.'.format(len(self.Targets)))

        if len(self.Targets) == 0:
            raise TargetsFileEmptyError()


    def __pickRandomProxy(self):
        """Elija al azar un proxy de la lista"""
        if not self.Proxies or len(self.Proxies) == 0:
            raise ProxiesFileEmptyError()

        self.__configureProxy(random.choice(self.Proxies))


    def __pickRandomUserAgent(self):
        """Elija aleatoriamente una cadena de agente de usuario de la lista"""
        if not self.UserAgents or len(self.UserAgents) == 0:
            raise UserAgentFileEmptyError()

        self.UserAgent = random.choice(self.UserAgents)
