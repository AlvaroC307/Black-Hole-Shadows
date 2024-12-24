
## Cosas general que mirar

- Mirar que paquete es numba, que pone que va veces mas rapido que python basico
- El paso adaptativo que vaya multiplicado por r o algo¿?
- Comprobaciones de como es una geodésica en el límite del agujero negro


# Ideas para mejorar el programa: 

## Version 1.0x:
- Ejes del gráfico
- Funcion propia para horizonte de eventos?
- Funcion subir y bajar indices?
- Comprobar que los parametros M,a,... sean numeros para que el usuario no borre el programa con eval()
- La metrica de Kerr-Newman de la base de datos está mal.    Yo del futuro:¿en serio?	Yo del futuro2: khe? Los Christoffel o como?
- Añadir un input que permita al usuario elegir si quiere que se saque la métrica de la base de datos o de la que ha creado él mismo. Para ello se puede crear una carpeta fantasma en Data_Base_Position_Total en la que se guarde una copia de la información en caso de que algo del programa falle. Este fichero se reinicia cada vez que se use esta función
- Añadir las Data_Base que faltan
- Añadir un agujero negro perturbado
- Cambiar el programa a que use (t,r,theta,phi) como una persona normal (HACERLO EN UN FICHERO APARTE POR SI SE JODE ALGO IMPORTANTE SIN QUERER)
- Arreglar el nombre de Cristoffel.py

## Version 1.x:
- Parametros de Horizon en función de M? Paso adaptativo en funcion de M?
- Si es un ordenador con más de 8 nucleos, que se divida en mas trabajadores. Yo del futuro2: Se puede pedir al usuario que de su número de nucleos y coger algo tipo n_nucleos-2 
- Cambio de angulo a x,y genérico no solo para tipo Kerr (Yo del futuro2: Con que función y cómo?)
- Que reciba la métrica desde un fichero metric.csv en la carpeta Input (Yo del futuro2: parte de esto está hecho en el trabajo de Gravitacion Avanzada)
- Renombrar y reescribir parte del programa para que sea más fácilmente legible. Preguntar a Mario convenciones?
- Implementar la opcion de que se vea graficamente el recorrido que hace una geodesica específica (Trabajo de Gravitación Avanzada)

## Version x.0:
- Aceptar métricas numéricas (Yo del futuro2: xdd, esto es con diferencia lo más jodido)
- Añadir Disco de Acrección


# Pruebas que hacer para entender mejor el programa:
-   Ver como cambia al cambiar theta_0, es posible que haya problema con el background (revisar) (problema cuando cambia phi_0 hay fijo)
-   Probar el programa con varios valores de M, los parametros Horizon y el paso adaptativo no estan en funcion de M