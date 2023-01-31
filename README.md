# Black-Hole-Shadows
Programa para el TFG sobre sombras de agujeros negros

IMPORTANTE: Las coordenadas van en el siguiente orden: t,r,phi,theta

Descripcion corta de los programas

Metric.py utiliza Sympy para escribir una metrica analitica en forma de matriz para luego extraerla en otros ficheros si es necesario

Cristoffel.py (si, esta mal escrito, falta una h), utiliza dicha metrica analitica y la utiliza para obtener los simbolos de christoffel, ya que estos son necesarios para resolver la ecuacion de las geodesicas general

Function_Metric.py define la metrica y la metrica inversa como funciones, para poder estar usandolas en otros ficheros sin problema. También define una funcion para los simbolos de christoffel, he revisado y deberían estar bien, no se si se pueden pasar automaticamente desde Cristoffel.py, preguntar y buscar en google. 

Momento_Temporal_Inicial.py es simplemente una funcion para obligar que la geodésica sea luminica, forzando un momento temporal inicial, o otros momentos que puedan ser necesarios.

Solving Hamiltonian Equations.py, recibe las ecuaciones de hamilton de una metrica analitica donde se hallan obtenido, y mediante las ccondiciones finales lleva el rayo de luz atrás en el tiempo para ver si tenderia al agujero negro o no. Estas 8 ecuaciones están ahora mismo escritas para el caso de Kerr, por lo que en vez de resolver 8 ecuaciones son 6, ya que p_t y p_phi son constantes en el parametro afin, y ya se tiene en cuenta con las constantes. Ademas, está definida la constante de Carter, asi que solo sirve para metricas tipo Kerr



Equations_to_Solve_Christoffel.py, crea las 8 ecuaciones lineales de las geodesicas en general, utilizando los simbolos de christoffel de Function_Metric.py

Solving_Kerr_with_Christoffel.py, es una función para resolver las ecuaciones de las geodesicas generales mediante un método RK4, cada resolución se van adaptando p^r y p^theta para mantener constante a las constantes necesarias en el caso analítico de Kerr, si fuera un caso en general solo se cambiaría una de esas constantes. El bucle de resolución con el RK4, se para cuando llega al horizote de eventos de un agujero negro de Kerr en específico, esto habrá que cambiarlo para una resolución general. 


Angle_to_Momentum.py es un fichero que se encargará de tener una función que cambie los ángulos definidos en un entorno de Minkowski alrededor de la pantalla, los cambia a los tres momentos p_r, p_phi, p_theta en coordenadas de Boyer-Lindquist


Black Hole Shadows.py es el fichero final, que utiliza el resto para devolver la imagen de un agujero negro con sus detalles correspondientes.



Ahora mismo, estos ficheros son para metricas analiticas tipo Kerr, en caso de querer metricas numericas, su variacion numerica se llamaran: N_fichero.py