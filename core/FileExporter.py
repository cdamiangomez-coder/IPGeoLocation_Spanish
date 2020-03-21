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

import csv
from xml.etree import ElementTree as etree
from collections import OrderedDict

class FileExporter:

    def __init__(self):
        pass

    def ExportListToCSV(self, ipGeoLocObjs, filename):
        return self.__ExportToCSV(ipGeoLocObjs, filename)

    def ExportToCSV(self, ipGeoLocObj, filename):
        return self.__ExportToCSV([ipGeoLocObj], filename)

    def ExportListToXML(self, ipGeoLocObjs, filename):
        return self.__ExportToXML(ipGeoLocObjs, filename)

    def ExportToXML(self, ipGeoLocObj, filename):
        return self.__ExportToXML([ipGeoLocObj], filename)

    def ExportListToTXT(self, ipGeoLocObjs, filename):
        return self.__ExportToTXT(ipGeoLocObjs, filename)

    def ExportToTXT(self, ipGeoLocObj, filename):
        return self.__ExportToTXT([ipGeoLocObj], filename)

    def __ExportToTXT(self, ipGeoLocObjs, filename):
        try:
            with open(filename, 'w') as txtfile:
                txtfile.write('Resultados Geolocalización de IP\n')
                for ipGeoLocObj in ipGeoLocObjs:
                    if ipGeoLocObj:
                        txtfile.write('Objetivo: {}\n'.format(ipGeoLocObj.Query))
                        txtfile.write('IP: {}\n'.format(ipGeoLocObj.IP))
                        txtfile.write('ASN: {}\n'.format(ipGeoLocObj.ASN))
                        txtfile.write('Ciudad: {}\n'.format(ipGeoLocObj.City))
                        txtfile.write('País: {}\n'.format(ipGeoLocObj.Country))
                        txtfile.write('Código País}: {}\n'.format(ipGeoLocObj.CountryCode))
                        txtfile.write('ISP: {}\n'.format(ipGeoLocObj.ISP))
                        txtfile.write('Latitud: {}\n'.format(ipGeoLocObj.Latitude))
                        txtfile.write('Longitud: {}\n'.format(ipGeoLocObj.Longtitude))
                        txtfile.write('Organización: {}\n'.format(ipGeoLocObj.Organization))
                        txtfile.write('Region: {}\n'.format(ipGeoLocObj.Region))
                        txtfile.write('Nombre Region: {}\n'.format(ipGeoLocObj.RegionName))
                        txtfile.write('Zona Horaria: {}\n'.format(ipGeoLocObj.Timezone))
                        txtfile.write('Código Postal: {}\n'.format(ipGeoLocObj.Zip))
                        txtfile.write('Google Maps: {}\n'.format(ipGeoLocObj.GoogleMapsLink))
                        txtfile.write('\n')
            return True
        except:
            return False


    def __ExportToXML(self, ipGeoLocObjs, filename):
        try:
            root = etree.Element('Resultados')

            for ipGeoLocObj in ipGeoLocObjs:
                if ipGeoLocObj:
                    orderedData = OrderedDict(sorted(ipGeoLocObj.ToDict().items()))
                    self.__add_items(etree.SubElement(root, 'IPGeolocation'),
                      ((key.replace(' ', ''), value) for key, value in orderedData.items()))

                    tree = etree.ElementTree(root)

            tree.write(filename, xml_declaration=True, encoding='utf-8')

            return True
        except:
            return False


    def __ExportToCSV(self, ipGeoLocObjs, filename):
        try:
            with open(filename, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
                writer.writerow(['Resultados', 'IPGeolocation'])
                for ipGeoLocObj in ipGeoLocObjs:
                    if ipGeoLocObj:
                        writer.writerow(['Objetivo', ipGeoLocObj.Query])
                        writer.writerow(['IP', ipGeoLocObj.IP])
                        writer.writerow(['ASN', ipGeoLocObj.ASN])
                        writer.writerow(['Ciudad', ipGeoLocObj.City])
                        writer.writerow(['País', ipGeoLocObj.Country])
                        writer.writerow(['Código País', ipGeoLocObj.CountryCode])
                        writer.writerow(['ISP', ipGeoLocObj.ISP])
                        writer.writerow(['Latitud', ipGeoLocObj.Latitude])
                        writer.writerow(['Longitud', ipGeoLocObj.Longtitude])
                        writer.writerow(['Organización', ipGeoLocObj.Organization])
                        writer.writerow(['Region', ipGeoLocObj.Region])
                        writer.writerow(['Nombre Region', ipGeoLocObj.RegionName])
                        writer.writerow(['Zona Horaria', ipGeoLocObj.Timezone])
                        writer.writerow(['Código Postal', ipGeoLocObj.Zip])
                        writer.writerow(['Google Maps', ipGeoLocObj.GoogleMapsLink])
                        writer.writerow([])
            return True
        except:
            return False


    def __add_items(self, root, items):
        for name, text in items:
            elem = etree.SubElement(root, name)
            elem.text = text
