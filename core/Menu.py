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

__autor__   = 'maldevel'
__twitter__  = '@maldevel'
__version__  = '2.0.4'
__año__     = '2015-2016'
__español__ = '@cdamiangomez'


from argparse import RawTextHelpFormatter
import argparse, os
from urllib.parse import urlparse
from core.Logger import Red


banner = """
{0}

{1} Obtener Información de Geolocalización de Ip desde ip-api.com
{1} Copyright (c) {2} {3} ({4})
{1} ip-api.com, el servicio prohibirá automáticamente cualquier dirección IP que realice más de 150 solicitudes por minuto.
{1} Traducido al Español por Carlos Damián Gómez (@cdamiangomez)

""".format(Red('IPGeolocation ' + __version__), Red('--['), __año__, __autor__, __twitter__, __español__)


def checkFileRead(filename):
    """Verifique si el archivo existe y tenemos acceso para leerlo"""
    if os.path.isfile(filename) and os.access(filename, os.R_OK):
        return filename
    else:
        raise argparse.ArgumentTypeError("Archivo {} Inválido (El archivo no existe, permisos insuficientes o no es un archivo).".format(filename))


def checkFileWrite(filename):
    """Comprueba si podemos escribir en el archivo"""
    if os.path.isfile(filename):
        raise argparse.ArgumentTypeError("El archivo {} ya existe.".format(filename))
    elif os.path.isdir(filename):
        raise argparse.ArgumentTypeError("Carpeta provista. Por favor proporcione un archivo.")
    elif os.access(os.path.dirname(filename), os.W_OK):
        return filename
    else:
        raise argparse.ArgumentTypeError("No se puede modificar el archivo {} (Permisos insuficientes).".format(filename))


def checkProxyUrl(url):
    """Compruebe si la URL del proxy es válida"""
    url_checked = urlparse(url)
    if (url_checked.scheme not in ('http', 'https')) | (url_checked.netloc == ''):
        raise argparse.ArgumentTypeError('Proxy URL {} inválido (ejemplo: http://127.0.0.1:8080).'.format(url))
    return url_checked


parser = argparse.ArgumentParser(description=banner, formatter_class=RawTextHelpFormatter)

#pick target/s
parser.add_argument('-m', '--my-ip',
                    dest='myip',
                    action='store_true',
                    help='Obtener información de geolocalización para mi dirección IP.')

parser.add_argument('-t', '--target',
                    help='Dirección IP o dominio a analizar.')

parser.add_argument('-T', '--tlist',
                    metavar='file',
                    type=checkFileRead,
                    help='Una lista de objetivos de IP / Dominios, cada objetivo en una nueva línea.')


#user-agent configuration
parser.add_argument('-u', '--user-agent',
                    metavar='User-Agent',
                    dest='uagent',
                    default='IP2GeoLocation {}'.format(__version__),
                    help='Establecer el encabezado de solicitud de agente de usuario (default: IP2GeoLocation {}).'.format(__version__))

parser.add_argument('-U', '--ulist',
                    metavar='file',
                    type=checkFileRead,
                    help='Establecer el encabezado de solicitud de User-Agent Una lista de cadenas de User-Agent, cada cadena en una nueva línea.')


#misc options
parser.add_argument('-g',
                    action='store_true',
                    help='Open IP location in Google maps with default browser.')

parser.add_argument('--noprint',
                    action='store_true',
                    help='IPGeolocation imprimirá la información de Geolocalización IP en el terminal. Es posible decirle a IPGeolocation que no imprima resultados en el terminal con esta opción.')

parser.add_argument('-v', '--verbose',
                    action='store_true',
                    help='Habilitar salida detallada.')

parser.add_argument('--nolog',
                    action='store_true',
                    help='IPGeolocation guardará un archivo .log. Es posible decirle a IPGeolocation que no guarde esos archivos de registro con esta opción.')


#anonymity options
parser.add_argument('-x', '--proxy',
                    type=checkProxyUrl,
                    help='Configurar servidor proxy (example: http://127.0.0.1:8080)')

parser.add_argument('-X', '--xlist',
                    metavar='file',
                    type=checkFileRead,
                    help='Una lista de proxies, cada URL de proxy en una nueva línea.')


#export options
parser.add_argument('-e', '--txt',
                    metavar='file',
                    type=checkFileWrite,
                    help='Exportar resultados en formato TXT.')

parser.add_argument('-ec', '--csv',
                    metavar='file',
                    type=checkFileWrite,
                    help='Exportar resultados en formato CSV.')

parser.add_argument('-ex', '--xml',
                    metavar='file',
                    type=checkFileWrite,
                    help='Exportar resultados en formato XML.')


args = parser.parse_args()
