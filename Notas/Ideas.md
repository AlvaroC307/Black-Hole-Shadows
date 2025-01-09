
## Cosas general que mirar

- Mirar que paquete es numba, que pone que va veces mas rapido que python basico
- El paso adaptativo que vaya multiplicado por r o algo¿?
- Comprobaciones de como es una geodésica en el límite del agujero negro


# Ideas para mejorar el programa: 

## Version 1.0x:
- Ejes del gráfico
- Comprobar que los parametros M,a,... sean numeros para que el usuario no borre el programa con eval()
- La metrica de Kerr-Newman de la base de datos está mal.    Yo del futuro:¿en serio?	Yo del futuro2: khe? Los Christoffel o como?
- Añadir un input que permita al usuario elegir si quiere que se saque la métrica de la base de datos o de la que ha creado él mismo. Para ello se puede crear una carpeta fantasma en Data_Base_Position_Total en la que se guarde una copia de la información en caso de que algo del programa falle. Este fichero se reinicia cada vez que se use esta función
- Añadir las Data_Base que faltan
- Cambiar el programa a que use (t, r, theta, phi) como una persona normal (HACERLO EN UN FICHERO APARTE POR SI SE JODE ALGO IMPORTANTE SIN QUERER)
-Igual va más rapido si cuando divido los trabajadores, divido el eje y en 4 y el eje x en 2 en vez de al reves. COMPORBAR
-Cambiarle el nombre a Solving_Kerr_with_Christoffel.py es muy engorroso
-Actualizar funcionamiento, explicando los detalles de los programas nuevos (no usan menos, por qué alguna funcion o parámetro está reescrita y no se usa el mismo, etc)
- En Geodesic.py añadir la posibilidad de dar un valor de x e y del dibujo generado.
- En Geodesic.py y el demás añadidos para la simulación de la trayectoria revisar los comentarios y redundancias o inconsistencias
- En Geodesic.py revisar Dif_t_Horizon y Dif_r_Horizon. Se puede crear una funcion dinámica que elija los valores en funcion de la precision elegida. Así evitar que la particula piense que se cae al BH cuando solo se mueve si la precision es alta o que no funcione si la precision es baja. La implementación actual deja que desear, meter una función con un if.
- En Representation_Geodesic.py revisar el -phi_0 en Polar_plot para calcular x e y para ver si tiene sentido físico y no solo es para dejarlo bonito.
## Version 1.x:
- Añadir un agujero negro perturbado
- Parametros de Horizon en función de M? Paso adaptativo en funcion de M?
- Si es un ordenador con más de 8 nucleos, que se divida en mas trabajadores. Yo del futuro2: Se puede pedir al usuario que de su número de nucleos y coger algo tipo n_nucleos-2 
- Cambio de angulo a x,y genérico no solo para tipo Kerr (Yo del futuro2: Con que función y cómo?)
- Que reciba la métrica desde un fichero metric.csv en la carpeta Input (Yo del futuro2: parte de esto está hecho en algun trabajo)
- Renombrar y reescribir parte del programa para que sea más fácilmente legible. Preguntar a Mario convenciones?
- Hacer que la imagen Background funcione para theta!=pi/2
- Añadir un archivo que permita ver cual es el origen de cada pixel de la imagen deformada. Es decir, genera la grafica actual, permite al usuario especificar x e y pixel en dicha imagen (añadir ejes del grafico con el numero de pixeles). Y utilizando lo mismo que se usa en Background_Image de Background calcula cual es el pixel original y lo marca en la figura sin deformar. (De momento solo idea) 

## Version x.0:
- Aceptar métricas numéricas (Yo del futuro2: xdd, esto es con diferencia lo más jodido)
- Añadir Disco de Acrección
- Implementar una interfaz

# Pruebas que hacer para entender mejor el programa:
-   Ver como cambia al cambiar theta_0, es posible que haya problema con el background (revisar) (problema cuando cambia phi_0 hay fijo)
-   Probar el programa con varios valores de M, los parametros Horizon y el paso adaptativo no estan en funcion de M


# Ideas desechadas:
- Funcion propia para horizonte de eventos
- Funcion subir y bajar indices
