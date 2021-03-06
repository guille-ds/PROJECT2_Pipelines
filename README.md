![satellite_Terra_pic](/input/pic.png)

# PROJECT 2 /// Tracking Satellites  

En este proyecto se busca **situar en tiempo real la posición de un satélite** en coordenadas terrestres (latitud, longitud, altitud). Para ello se utiliza un **Dataset y una API**.

### **DATASET**
El dataset, producido por la UCS y actualizado a 16 de Diciembre de 2019, contiene 2218 registros de los satélites actualmente en órbita, catalogados según su nombre oficial, datos sobre su lanzamiento (fecha, país, plataforma, empresa), datos sobre su órbita (LEO/GEO, periodo, ascendente, descendente) y *NORAD id* (cifra identificativa de cada objeto en órbita, asignado por la *USCC (United States Space Command)*).
Ha sido limpiado para este proyecto de modo que se facilite su lectura.

### **API**
La API es la *REST API v1 de N2YO* que cuenta con distintos métodos para la localización de satélites de forma gratuita, mediante una APIKey y con una restrición de 1000 requests/hora.
###### Consigue una APIKey registrándote [aquí](https://www.n2yo.com/login/)


### **FUNCIONAMIENTO**

Se ejecuta **main.py** desde la línea de comandos y se introducen 3 flags:

- País (de procedencia del satélite)
- Año (de lanzamiento)
- Segundos (durante los cuales se trackeará el satélite)

*Ej:*  `$ python3 main.py USA 2010 2`  -  Filtra los satélites lanzados por *USA* en *2010* y devuelve *2* posiciones.

Se produce el filtrado del dataset en base a los dos primeros campos introducidos y se muestra en la terminal los satélites que pasan el filtro.
El usuario introduce el número de registro del satélite a trackear, lo cual ejecuta una request a la API, que devuelve un diccionario con la posición geolocalizada del satélite.
A dicha información se le añade la provista por el registro del satélite elegido en el dataset y se muestra en pantalla.

### **DIRECCIONES DE MEJORA**

- Limitar la entrada de filtros añadiendo *try/except*
- Añadir otros flags para un filtrado basado en otros parámetros presentes en el Dataset.
- Mejorar la versatilidad añadiendo distintos modos de trackeo o requests a la API, pues cuenta con 3 modos más (*Visual passes, Radio passes, What's up*)
- Exportación en pdf de la información y/o envío de mail con pdf adjunto.
- Incluir marcación de posición en mapa (*Folium* no permite exportación directa aunque con *Selenium* se podría conseguir captura de pantalla o guardado de imagen desde explorador.)


![Folium test pic](/input/pic2.png)
###### *Test de tracking de NORADid:43935 (4 de Febrero a las 13:51 durante 3 segundos) representado en Folium.*


### **LINKS**

- Dataset https://www.ucsusa.org/resources/satellite-database
- API https://www.n2yo.com/api/#positions

