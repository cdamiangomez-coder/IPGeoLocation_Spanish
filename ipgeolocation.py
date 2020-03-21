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

__author__  = 'maldevel'
__español__ = 'cdamiangomez'


import sys, os
from core.IpGeoLocationLib import IpGeoLocationLib
from core.Logger import Logger
from core.Menu import parser,args,banner

def main():

    # no args provided
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    logsDir = os.path.join(os.getcwd(), 'logs')
    #resultsDir = os.path.join(os.getcwd(), 'results')
    if not os.path.exists(logsDir):
        os.mkdir(logsDir)
    #if not os.path.exists(resultsDir):
    #    os.mkdir(resultsDir)

    logger = Logger(args.nolog, args.verbose)

    #single target or multiple targets
    if(args.target and args.tlist):
        logger.PrintError("Puede solicitar información de geolocalización para un solo target(-t) o una lista de targets(-T). No ambos!", args.nolog)
        sys.exit(2)

    #my ip address or single target
    if(args.target and args.myip):
        logger.PrintError("Puede solicitar información de geolocalización para un solo target(-t) o tu propia Dirección IP. No ambos!", args.nolog)
        sys.exit(3)

    #multiple targets or my ip address
    if(args.tlist and args.myip):
        logger.PrintError("Puede solicitar información de geolocalización para obtener de una lista de targets(-T) o tu propia Dirección IP. No ambos!", args.nolog)
        sys.exit(4)

    #single target and google maps only allowed
    if(args.tlist and args.g):
        logger.PrintError("La ubicación de Google Maps solo funciona con objetivos únicos.", args.nolog)
        sys.exit(5)

    #specify user-agent or random
    if(args.uagent and args.ulist):
        logger.PrintError("Puede especificar una cadena de agente de usuario o dejar que IPGeolocation elija cadenas de agente de usuario aleatorias de un archivo.", args.nolog)
        sys.exit(6)

    #specify proxy or random
    if(args.proxy and args.xlist):
        logger.PrintError("Puede especificar un proxy o dejar que IPGeolocation elija conexiones de proxy aleatorias para usted de un archivo.", args.nolog)
        sys.exit(7)


    #init lib
    ipGeoLocRequest = IpGeoLocationLib(args.target, logger, args.noprint)

    print(banner)

    #retrieve information
    if not ipGeoLocRequest.GetInfo(args.uagent, args.tlist,
                                     args.ulist, args.proxy, args.xlist,
                                     args.csv, args.xml, args.txt, args.g):
        logger.PrintError("No se pudo recuperar la información de geolocalización de IP.")
        sys.exit(8)


if __name__ == '__main__':
    main()
