# IPGeoLocation - Traducido al Español
====
* La herramienta obtiene información sobre la GeoLocalización de una IP especifica o Varias.
* Powered by [ip-api](http://ip-api.com/docs/)


Requerimientos
=====
* Python 3.x
* termcolor
* colorama


Descarga-Instalación
====
Original (en inglés) TW: @maldevel
* git clone https://github.com/cdamiangomez-coder/IPGeoLocation_Spanish

Traducido al español TW: @cdamiangomez
* git clone https://gtihub.com/cdamiangomez-coder/IPGeoLocation_Spanish 

* pip3 install -r requirements.txt --user

Si no está instalado pip3:
* apt-get install python3-setuptools
* easy_install3 pip
* pip3 install -r requirements.txt


Caracteristicas
====
* Recuperar IP o Geolocalización de Dominio.
* Recupere su propia geolocalización IP.
* Recuperar Geolocalización para IPs o Dominios cargados del archivo. Cada objetivo en nueva línea.
* Defina su propia cadena de agente de usuario personalizada.
* Seleccione cadenas aleatorias de User-Agent del archivo. Cada cadena de agente de usuario en una nueva línea.
* Soporte de proxy.
* Seleccione proxy aleatorio del archivo. Cada URL proxy en una nueva línea.
* Abra la geolocalización de IP en Google Maps usando el navegador predeterminado.
* Exportar resultados a formato csv, xml y txt.

Información sobre Geolocalización
====
* ASN
* Ciudad
* País
* Código del País
* ISP
* Latitud
* Longitud
* Organización
* Codigo de Región
* Nombre de Región
* Zona Horaria
* Código Postal


Modo de Uso
====
```
$ ./ip2geolocation.py
Modo de uso: ipgeolocation.py [-h] [-m] [-t TARGET] [-T file] [-u User-Agent]
                        [-U file] [-g] [--noprint] [-v] [--nolog] [-x PROXY]
                        [-X file] [-e file] [-ec file] [-ex file]

IPGeolocation 2.0.4

--[ Obtener Información de Geolocalización de Ip desde ip-api.com
--[ Copyright (c) 2015-2016 maldevel (@maldevel)
--[ ip-api.com, el servicio prohibirá automáticamente cualquier dirección IP que realice más de 150 solicitudes por minuto.
--[ Traducido al Español por Carlos Damián Gómez (@cdamiangomez)

optional arguments:
  -h, --help            Muestra este mensaje y se cierra.
  -m, --my-ip           Obtener información de geolocalización para mi dirección IP.
  -t TARGET, --target TARGET
                        Dirección IP o dominio a analizar.
  -T file, --tlist file
                        Una lista de objetivos de IP / Dominios, cada objetivo en una nueva línea.
  -u User-Agent, --user-agent User-Agent
                        Establecer el encabezado de solicitud de agente de usuario (default: IP2GeoLocation 2.0.4).
  -U file, --ulist file
                        Establecer el encabezado de solicitud de User-Agent Una lista de cadenas de User-Agent, cada cadena en una nueva línea.
  -g                    Open IP location in Google maps with default browser.
  --noprint             IPGeolocation imprimirá la información de Geolocalización IP en el terminal. Es posible decirle a IPGeolocation que no imprima resultados en el terminal con esta opción.
  -v, --verbose         Habilitar salida detallada.
  --nolog               IPGeolocation guardará un archivo .log. Es posible decirle a IPGeolocation que no guarde esos archivos de registro con esta opción.
  -x PROXY, --proxy PROXY
                        Configurar servidor proxy (example: http://127.0.0.1:8080)
  -X file, --xlist file
                        Una lista de proxies, cada URL de proxy en una nueva línea.
  -e file, --txt file   Exportar resultados en formato TXT.
  -ec file, --csv file  Exportar resultados en formato CSV.
  -ex file, --xml file  Exportar resultados en formato XML.

```
  

Ejemplos
====
**Obtener la Geolocalización de tu IP**
* ./ip2geolocation.py -m

**Obtener la Geolocalización de una IP**
* ./ip2geolocation.py -t x.x.x.x

**Obtener la Geolocalización de un Dominio**
* ./ip2geolocation.py -t ejemplo.com

**No guardar el archivo .log**
* ./ip2geolocation.py -t ejemplo.com --nolog

**Cadena de agente de usuario personalizado** 
* ./ip2geolocation.py -t x.x.x.x -u "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0)"

**Usando Proxy**
* ./ip2geolocation.py -t x.x.x.x -x http://127.0.0.1:8080

**Usando Proxy aleatorio**
* ./ip2geolocation.py -t x.x.x.x -X /carpeta/de/proxys/nombre_archivo.txt

**Pick User-Agent string randomly**
* ./ip2geolocation.py -t x.x.x.x -U /carpeta/de/nombres-usuario/nombre_archivo.txt

**Obtener la ubicación geográfica de IP y la ubicación abierta en los mapas de Google con el navegador predeterminado**
* ./ip2geolocation.py -t x.x.x.x -g

**Exportar los resultados a un archivo con formato CSV**
* ./ip2geolocation.py -t x.x.x.x --csv /carpeta/de/resultados.csv

**Exportar los resultados a un archivo con formato XML**
* ./ip2geolocation.py -t x.x.x.x --xml /carpeta/de/resultados.xml

**Exportar los resultados a un archivo con formato TXT**
* ./ip2geolocation.py -t x.x.x.x -e /carpeta/de/resultados.txt

**Obtener la geolocalización de IP para muchos objetivos**
* ./ip2geolocation.py -T /carpeta/de/objetivos/objetivos.txt

**Recupere la geolocalización de IP para muchos objetivos y exporte resultados a xml**
* ./ip2geolocation.py -T /carpeta/de/objetivos/objetivos.txt --xml /carpeta/de/resultados.xml

**No mostrar resultados en la terminal**
* ./ip2geolocation.py -m -e /path/to/results.txt --noprint 
