# Black-Hole-Shadows
Programa para el TFG sobre sombras de agujeros negros

Metric.py utiliza Sympy para escribir una metrica analitica en forma de matriz para luego extraerla en otros ficheros si es necesario

Cristoffel.py (si, esta mal escrito, falta una h), utiliza dicha metrica analitica y la usa para obtener los simbolos de christoffel, ya que estos son necesarios para resolver la ecuacion de las geodesicas

Solving Hamiltonian Equations.py, recibe las ecuaciones de hamilton de una metrica analitica donde se hallan obtenido, y mediante las ccondiciones finales lleva el rayo de luz atrás en el tiempo para ver si tenderia al agujero negro o no. Estas 8 ecuaciones están ahora mismo escritas para el caso de Kerr, por lo que en vez de resolver 8 ecuaciones son 6, ya que p_t y p_phi son constantes en el parametro afin, y ya se tiene en cuenta con las constantes. Ademas, está definida la constante de Carter, asi que solo sirve para metricas tipo Kerr

Black Hole Shadows.py es el fichero final, que utiliza el resto para devolver la imagen de un agujero negro con sus detalles correspondientes.

Ahora mismo, estos ficheros son para metricas analiticas tipo Kerr, en caso de querer metricas numericas, su variacion numerica se llamaran: N_fichero.py