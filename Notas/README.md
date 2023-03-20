# Black-Hole-Shadows
Programa para el TFG sobre sombras de agujeros negros

IMPORTANTE: Las coordenadas van en el siguiente orden: t, r, phi, theta

Descripcion corta de los programas:

Metric.py utiliza Sympy para escribir una metrica y su inversa de manera analitica en forma de matriz para luego extraerla en otros ficheros.

Cristoffel.py (si, esta mal escrito, falta una h), utiliza dicha metrica analitica y la utiliza para obtener los simbolos de christoffel, ya que estos son necesarios para resolver la ecuacion de las geodesicas general. A veces, tarda en compilar. 

Function_Metric.py define la metrica y la metrica inversa como funciones, para poder estar usandolas en otros ficheros sin problema. También define una funcion para los simbolos de Christoffel. 

Momento_Temporal_Inicial.py es simplemente una funcion para obligar que la geodésica sea luminica, forzando un momento temporal inicial, u otros momentos que puedan ser necesarios.

Equations_to_Solve_Christoffel.py, crea las 8 ecuaciones lineales de las geodesicas en general, utilizando los simbolos de christoffel de Function_Metric.py y añadiendo a cada una un menos porque se resuelve la geodesica hacia atras en el parametro de
la curva.

Solving_Kerr_with_Christoffel.py, es una función para resolver las ecuaciones de las geodesicas generales mediante un método RK4. Cada resolución se van adaptando p^r y p^theta para mantener constante a las constantes necesarias en el caso analítico de Kerr. En un caso en general solo se cambiaría . Tambien tiene un paso adaptativo en funcion de la coordenada radial y para evitar la singularidad del eje sin(theta)=0. El horizonte de eventos se define si varia mucho la coordenada temporal o la radial de golpe. Escapar del agujero negro se define como: coordenada radial mayor a un r_limit y aumentando, tras esto se calcula el color en función del cuadrante del espacio-tiempo en el que se encuentre.

Angle_to_Momentum.py es un fichero que se encarga de tener una función que cambia las coordenadas definidas en un entorno local de Minkowski alrededor de la pantalla. Calcula los tres momentos p_r, p_phi, p_theta en coordenadas de Boyer-Lindquist y luego utiliza Momento_Temporal_Inicial para calcular p_t.

Background.py es un fichero que comprueba en que cuadrante de la esfera celestial ha caido el foton y así poder ver como se deforma el agujero negro.

Shadow_MultiProcess.py es el fichero final. Utiliza el resto de resultados para devolver el color de cada pixel de la imagen de un agujero negro con sus detalles correspondientes. Para ello utiliza un multiproceso con 8 trabajadores y poder calcular la sombra del agujero negro más rápidamente. La pantalla se divide en 4 workers para (L_screen, 0) y otros 4 en (0, -L_screen).

Representacion.py es el fichero que se ejecuta al final para poder observar el resultado del resto del programa. Grafica los puntos
que se han calculado con una serie de colores para ver la forma de la sombra y como el agujero negro deforma el espacio-tiempo cercano. Tras esto guarda una imagen png y otra pdf en la carpeta Graphics.



Ahora mismo, estos ficheros son para metricas analiticas tipo Kerr, en caso de querer metricas numericas, su variacion numerica se llamaran: N_fichero.py