# VERSION ACTUAL--> 2.12

Explicacion de como ejecutar los programas correctamente:

# MÉTRICAS ANALÍTICAS:

##### Primer paso: 
    Escribir la métrica analítica que se quiera comprobar en el archivo Metric.py en cada uno de los 16 g_munu (g00,g01,g02,...) el programa esta escrito de tal manera que las coordenadas vayan en el siguiente orden: t-r-phi-theta

##### Segundo paso: 
    Ejecutar el programa Metric.py, con ello se obtiene la métrica inversa y se escriben los elementos de la métrica y la métrica inversa en dos ficheros

##### Tercer paso: 
    Ejecutar el programa Cristoffel.py, este programa escribe los 64 símbolos de christoffel necesarios en otro fichero, los tres ficheros que se acaban de escribir estarán disponibles en la carpeta Data

##### Cuarto paso: 
    Introducir en el fichero Input los datos referentes al agujero negro que se quiera calcular la sombra. También se debe introducir el número de Pixeles, siendo una imagen N_pix*N_pix, depende del detalle que se quiera en la imagen. El factor Factor_Screen es el factor multiplicativo a una pantalla que mida exactamente el tamaño de la sombra de Schwarzschild se recomienda un Factor_Screen de 3 o 4. Back_Im toma valor C si quiere usar la funcion que define cada cuadrante de la esfera de un color, y toma valor I si quieres proporcionar una imagen para usar de fondo. Introducir tambien los parametros del espacio tiempo en Extra_Constants.csv (a, Q, Lambda,....). name pide el nombre de la métrica para utilizar los simbolos directamente de la base de datos.
             
##### Quinto paso: 
    Ejecutar el fichero Shadow_Multiprocess.py que devuelve los datos del color del pixel y su posición en la carpeta Data para realizar comprobaciones.

##### Sexto paso: 
    Ejecutar el fichero Representacion.py, este sirve para hacer un dibujo con los colores de los pixeles calculados y lo muestra en pantalla. Lo guarda en la carpeta Graphics como Black_Hole_Image.png


## Cambiar el fondo de una imagen sin simular de nuevo el agujero negro

-------------------------------------------EN CONSTRUCCION-------------------------------------


# Geodésicas Específicas

-------------------------------------------EN CONSTRUCCION-------------------------------------

