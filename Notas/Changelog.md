# Versiones Alpha

## Alpha 0.1
    Desarrollo de Christoffel.py y Metric.py mediante sympy
#### Alpha 0.11 
    Cambio de la manera de llamar a los elementos de las matrices G e Inv_G, ahora funciona llamando a una matriz directamente
    
## Alpha 0.2  
    Desarrollo de Solving_Hamiltonian_Equations.py básico
#### Alpha 0.21 
    Arreglo de diversos errores de Solving_Hamiltonian_Equations y cambios para su generalización

# Versiones Beta

##    Beta 0.1  
    Desarrollo de Function_Metric.py y Solving_Kerr_With_Christoffel.py, a partir de ahora SWC.py, en vez de con el hamiltoniano, cambio completo de como resolver las geodésicas
####    Beta 0.11 
    Reescritura de Function_Metric.py para que el programa tome los simbolos de Christoffel automaticamente y no haya que pasarselos a mano 
####    Beta 0.12 
    Reescritura de Function.Metric.py para evitar programacion espaguetti, reduciendo el tamaño del fichero de 300 a 70 líneas totales
####    Beta 0.13 
    Diversas comprobaciones y eliminación de la parte del programa que cambiaba p^r y p^theta para mantener a m^2 y Q constantes

##    Beta 0.2  
    Cambio de SWC.py a una funcion para poder ejecutarlo en un futuro en Black_Hole_Shadows.py
####    Beta 0.21 
    SWC.py pasa a ser una función con 2 outputs

##    Beta 0.3  
    Escritura del programa Angle_to_Momentum.py especifico para la métrica de tipo Kerr
####    Beta 0.31 
    Escritura del programa Black_Hole_Shadows.py pero sin ser funcional completamente, no está bien definido los límites de la pantalla, no existe una barra de progreso y no se escribe en ningún fichero, versión simplificada

# Versiones Finales 1.0

##    Version 1.0  
    Escritura del programa Black_Hole_Shadows.py y primeras ejecuciones del programa para N_pix=10 y para N_pix=25. Añadido de comentarios sobre el progreso del programa
####    Version 1.01 
    Cambio del programa SWC.py para que pare el cálculo de las geodésicas cuando la coordenada radial está aumentando y es mayor que 10*M
####    Version 1.02
    Cambio del programa Black_Hole_Shadows.py para tomar los valores y parámetros de un fichero y así no cambiarlo cada vez que se haga una imagen nueva
####    Version 1.03 
    Generalización de Mom_temp para métricas no tipo Kerr. Paso Adaptativo para diversos valores de la coordenada radial
####    Version 1.04 
    Reañadido de la funcion Mom_Sum_r, haciendo una comprobacion en caso de que la raiz sea imaginaria, se asuma que ha caido al interior del agujero negro. Revisado y alterado el funcionamiento del paso adaptativo además de convertirlo en una función extra.

##    Version 1.1  
    Utilizando Minkowski a partir de r=10M, calcular en que cuadrante cae el fotón y su color, gracias a Backgroung.py. 
####    Version 1.11 
    Añadir un parámetro para decidir a partir de cuando se considera que la métrica es Minkowski y el fotón no vuelve al agujero negro.

##    Version 1.2  
    Creación del Plot en Python en el fichero Representacion.py. Comienzo del cambio de Black Hole Shadows para que vaya más rápido usando varios nucleos, estos cambios se hicieron en otro fichero para que el programa siguiera funcionando en caso de problema y para poder realizar comparaciones. Primeras imagenes con el color de deformación del espacio-tiempo, N_pix=50.
####    Version 1.21 
    Cambio de la definición de Horizonte de Eventos, ahora en vez de mirar cuando se dispara el tiempo comprueba cuando g_rr camia de signo y se hace negativa
####    Version 1.22 
    Arreglo del bug que hacía que se representara verticalmente. Arreglo del bug que hacia que se representara espejado, para ello he quitado el menos de la definición de ps_phi_0 y ps_theta_0
####    Version 1.23 
    Añadido un código para guardar la imagen en un archivo .eps y creado un fichero para pasar la imagen de eps a jpg
####    Version 1.24 
    Solucionado el problema en el eje sin(theta)=0, mediante un cambio en el paso adaptativo cuando theta=0 o theta=pi. Revertido el cambio de la version 1.21 porque daba problemas. Añadido ciertas condiciones a la definición de horizonte de eventos para evitar pixeles mal.

##    Version 1.3  
    Arreglo de la barra de progreso, ahora va para cada worker. Cambio del fichero Representation.py para que funcione con matplotlib y guarde una imagen png y otra pdf, el fichero Eps_to_Jpg ahora es redundante. Limpiar la carpeta de codigos y archivos inútiles. Añadido Factor_Screen para que el usuario en Input cambie el tamaño deseado de la pantalla. Limpieza y comentarios de la mayoria de codigos excepto Angle_to_Momentum y Momento_Temporal_Inicial porque hay que repasar ambos programas más. Cambio del nombre del programa principal a Shadow_Multiprocess.
####    Version 1.31 
    Añadido de un sonido al acabar el programa Shadow_Multiprocess.py.
####    Version 1.32 
    Comienzo de una funcion alternativa a Sphere_Quadrants, para si el usuario quiere dar una imagen de fondo el mismo. Añadido de un parámetro en el Input.csv, que puede tomar valores "C" (colores) si se quiere usar la funcion Sphere_Quadrants, o "I" (Image) si se quiere usar la nueva función Background_Image. No está todavía operativa.

##    Version 1.4  
    Implementación completa de la nueva función Background_Image. Tanto en el ficher Shadow_Multiprocess.py como en el fichero Representation.py. Faltan de hacer pruebas con ella todavía para confirmar su correcto funcionamiento.
####    Version 1.41 
    Cambio de la funcion Background_Image porque representaba al revés el eje z, añadido del parametro N_pix a la funcion Geodesic_Chris y Background_Image.
####    Version 1.42 
    Añadido de los parametros Dif_t_Horizon y Dif_r_Horizon para cambiar más facil la definicion de Horizonte de Eventos
####    Version 1.43 
    Hay un nuevo parametro eps en la funcion Background_Image, suma una cantidad a L_I porque existe una posibilidad que r>r_limit, y por tanto se pase del numero de pixeles de la imagen. Creacion de una imagen con meridianos, paralelos y un circulo blanco en el centro. Cambio del color cuando se realiza el RK4 más de N veces a rosa.
####    Version 1.44 
    Comentarios en Angle_to_Momentum y algo de limpieza y comentarios en Momento_Temporal_Inicial. Cambio de la funcion Paso_adap para que el progama vaya un 25% más rapido. Cambio de la funcion paso_adap para que mire antes si se encuentra cerca del agujero negro, ya que se suele estar cerca y lejos pasa poco rato, asi evita comprobar muchos if.
    
##    Version 1.5  
    Generalizacion a un numero abitrario de parametros, faltan comprobaciones en Cristoffel.py y Metric.py. Nuevo fichero Initial_Values.py donde se lee Input y Extra_Constants para obtener todos los parametros necesarios para el codigo. Ahora en vez de mandar las constantes en las funciones las llama a especifico fichero. Facilidad de cambio de r_limit. Cambio de nombre a la cte de Carter. Limpieza de las funciones importadas.
####    Version 1.51 
    Añadido el typing a las funciones del programa principal, falta el calculo de los simbolos de Christoffel.
####    Version 1.52 
    Añadido de numpy en ciertas partes de Solving_Kerr_with_Chritoffel aunque no gana nada de tiempo. Cambio de la funcion paso_adap para que vaya bastante más rapido.
####    Version 1.53 
    Cambios pequeños y comprobacion del paso adaptativo, ahora en el eje sin(theta)=0 hace la comprobacion con el seno y no theta o theta-pi.
####    Version 1.54 
    Ahora tiene más tamaño la comprobacion en el eje para evitar ciertos errores puntuales. Primera imagen 200x200

##    Version 1.6  
    Ahora se guardan las coordenadas r, theta y phi de las geodesicas que se van a infinito. Para poder ejecutar el nuevo fichero Change_BackGround y poder cambiar el fondo de la imagen sin necesidad de ejecutar de nuevo Shadow_Multiprocess.
####    Version 1.61 
    Pequeño ajuste del paso adaptativo
####    Version 1.62 
    Generalizacion de la funcion Mom_Sum_r

# Versiones Finales 2.0

##    Version 2.0  
    Terminado el funcionamiento para métricas analíticas arbitrarias. Acepta Kerr_Newman y sale correctamente. Creada una base de datos de simbolos de Christoffel y de las propias métricas y sus inversas. Creado el parámetro name, es un string con el nombre de la carpeta de la base de datos que se vaya a usar. 
####    Version 2.0.1 
    Cambio del fichero background.py para que el nombre de la imagen de fondo se introduzca en Input
####    Version 2.0.2 
    Pequeña limpieza del código para quitar código comentado sin usar. Cambio de los nombres de Back_Im de "C" y "I" a "Colours" y "Image" para fácilitar la lectura del código. Además, añadido la función matplot a Shadow_Multiprocess.py 
    para que se nada más acabar se genere la imagen sin necesidad de ejecutar Representation.py por separado continuamente.
#### Version 2.0.3 
    Creación de una base de datos de los resultados, Data_Base_Position_Total donde guardar los agujeros negros más típicos. Reescritura del programa Change_Background.py para que utiilce la información de la base de datos. Actualizado los archivos en Notas para que esten en markdown y no txt.
#### Version 2.0.4
    Se ha arreglado el bug que no permitía generar un sonido al acabar. Se ha definido una funcion para ello y ahora el path al archivo de sonido se puede dar por el usuario. Arreglado el nombre del archivo Christoffel.py.

## Version 2.1
    Se han creado los ficheros Solving_Specific_Geodesic.py y Representation_Geodesic.py que simulan la trayectoria de una partícula (másiva o no) en el entorno de un agujero negro. Hay dos parámetros nuevos para estos cálculos: precision (precision de la computacion de la trayectoria) y m (masa de la partícula), además de dos alternativos r_limit_geodesic y r_0_geodesic.
#### Version 2.1.1
    Creado un fichero Input_Geodesic.csv para introducir datos relevantes específicos a la resolución de la trayectoria específica. Añadido la posibilidad de calcular una geodésica dados unos puntos x,y en la imagen, para ello hemos creado una función nueva en Angle_to_momentum con otra convención de signos ya que esto no es backwards Ray-Tracing. Cambiado las funciones de Angle_to_momentum para que devuelvan una tupla. Cambiado el nombre de Solving_Kerr_with_Christoffel.py a Solving_Geodesic_Backwards_RayT y limpiado parte de código desactualizado. Añadida una función en Representation_Geodesic.py que calcula el horizonte de eventos de los agujeros negros usuales
#### Version 2.1.2
    Añadido una opcion para poner ejes al grafico. Con ejes se puede ver el tamaño de la sombra del agujero negro y sin ellos se puede ver de que x,y se origina cada pixel. Simplificación importante de la funcion Screen en Shadow_Multiprocess.py. 
#### Version 2.1.3
    Arreglado la opcion de calcular una geodesica dados unos puntos x,y de la imagen. Comprobado que la elección de signos en Angle_to_Momentum.