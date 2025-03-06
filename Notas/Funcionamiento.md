# Explicacion de cada fichero del programa

Ahora mismo, estos ficheros son para metricas analiticas tipo Kerr, en caso de querer metricas numericas, su variacion numerica se llamaran: N_fichero.py

#### IMPORTANTE: Las coordenadas van en el siguiente orden: t, r, phi, theta

# Metric.py:  
    Utiliza Sympy para escribir una metrica y su inversa de manera analitica en forma de matriz para luego extraerla en otros ficheros.

# Cristoffel.py (si, esta mal escrito, falta una h):
    Utiliza dicha metrica analitica y la utiliza para obtener los simbolos de christoffel, ya que estos son necesarios para resolver la ecuacion de las geodesicas general. A veces, tarda en compilar. 

# Initial_Values.py: 
    Lee los ficheros de entrada, Input.csv y Extra_Constants.csv y almacena los datos en unas constantes que luego se pueden referenciar directamente. Como las constantes pueden ser un numero arbitrario con nombre dado por el usuario se almacenan en un diccionario.

# Function_Metric.py:
    Define la metrica y la metrica inversa como funciones, para poder estar usandolas en otros ficheros sin problema. También define una funcion para los simbolos de Christoffel. 

# Momento_Temporal_Inicial.py:
    Es simplemente una funcion para obligar que la geodésica sea luminica, forzando un momento temporal inicial, u otros momentos que puedan ser necesarios.

# Equations_to_Solve_Christoffel.py:
    Crea las 8 ecuaciones lineales de las geodesicas en general, utilizando los simbolos de christoffel de Function_Metric.py y añadiendo a cada una un menos porque se resuelve la geodesica hacia atras en el parametro de la curva.

# Solving_Geodesic_Backwards_RayT.py:
    Es una función para resolver las ecuaciones de las geodesicas generales mediante un método RK4. Cada resolución se van adaptando p^r y p^theta para mantener constante a las constantes necesarias en el caso analítico de Kerr. En un caso en general solo se cambiaría . Tambien tiene un paso adaptativo en funcion de la coordenada radial y para evitar la singularidad del eje sin(theta)=0. El horizonte de eventos se define si varia mucho la coordenada temporal o la radial de golpe. Escapar del agujero negro se define como: coordenada radial mayor a un r_limit y aumentando, tras esto se calcula el color en función del cuadrante del espacio-tiempo en el que se encuentre.

# Angle_to_Momentum.py:
    Es un fichero que se encarga de tener una función que cambia las coordenadas definidas en un entorno local de Minkowski alrededor de la pantalla. Calcula los tres momentos p_r, p_phi, p_theta en coordenadas de Boyer-Lindquist y luego utiliza Momento_Temporal_Inicial para calcular p_t.

# Background.py:
    Es un fichero que comprueba en que cuadrante de la esfera celestial ha caido el foton y así poder ver como se deforma el agujero negro.

# Shadow_MultiProcess.py:
    Es el fichero final. Utiliza el resto de resultados para devolver el color de cada pixel de la imagen de un agujero negro con sus detalles correspondientes. Para ello utiliza un multiproceso con 8 trabajadores y poder calcular la sombra del agujero negro más rápidamente. La pantalla se divide en 4 workers para (L_screen, 0) y otros 4 en (0, -L_screen).

# Representacion.py:
    Es el fichero que se ejecuta al final para poder observar el resultado del resto del programa. Grafica los puntos que se han calculado con una serie de colores para ver la forma de la sombra y como el agujero negro deforma el espacio-tiempo cercano. Tras esto guarda una imagen png y otra pdf en la carpeta Graphics.

# Change_Background.py:
    Este fichero lo puede activar el usuario cuando quiera cambiar la imagen de fondo que se usa en la simulacion. Para ello, utiliza los datos dados en Input.csv para accederal agujero negro correspondiente de la base de datos y usa los datos guardados para encontrar el color de los puntos que no han caido en el agujero negro.

# Solving_Specific_Geodesic.py
    Este fichero calcula la trayectoria de una única partícula alrededor del agujero negro. Para ello sigue el mismo algoritmo que Solving_Geodesic_Backwards_RayT.py con un par de diferencias. Por ejemplo, se ha añadido un parámetro para alterar la precisión del cálculo, se ha introducido un menos antes de llamar a la función Switch_punto puesto que en la definición dada en Equations_to_Solve_Christoffel.py se calculan las ecuaciones hacia atrás para el Backwards Ray-Tracing.
    
# Representation_Geodesic.py
    En este fichero se definen funciones para representar tres graficas de la trayectoria de una partícula cayendo a un agujero negro. La primera nos representa la coordenada radial esférica respecto al tiempo. La segunda nos representa el parámetro afín o tiempo propio respecto al tiempo y la ultima nos genera una grafica polar donde vemos claramente la trayectoria. Las lineas discontinuas rojas representan el horizonte de eventos. Se ha añadido un -phi_0 en Representacion_Geodesic.py en Polar_plot para incluir casos distintos de phi_0!=0 sin que el dibujo de un resultado extraño.

# Interface.py 
    Carga la Interfaz de uso sencillo de la aplicacion y una explicación de la misma