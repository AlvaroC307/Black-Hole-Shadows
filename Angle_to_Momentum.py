# Importar ficheros útiles
import math
from Function_Metric import G
import Momento_Temporal_Inicial as mti
from Initial_Values import t_0, r_0, phi_0, theta_0

# Ahora mismo será especifico a un agujero negro tipo Kerr, es decir: métrica diagonal excepto en los términos t-phi
# la matriz de transformación de la base del observador a la base coordenadas, calculamos los 5 elementos primero

def Screen_to_Momentum(x:float, y:float)->tuple:

    coords_0=(t_0, r_0, phi_0, theta_0) # Tupla de coordenadas iniciales


    # Calculo de los parametros para obtener x e y, sigue la notacion de Chaotic Shadows
    At=math.sqrt((G(2, 2, *coords_0))/(G(2, 0, *coords_0)**2-G(0, 0, *coords_0)*G(2, 2, *coords_0)))
    Ar=1/math.sqrt(G(1, 1, *coords_0))
    Aphi=1/math.sqrt(G(2, 2, *coords_0))
    Atheta=1/math.sqrt(G(3, 3, *coords_0))
    Gamma=-((G(2, 0, *coords_0))/(G(2, 2, *coords_0)))*At  

    # Tenemos las siguientes dos ecuaciones: x=(-r*ps_local_phi)/(ps_local_r), y=(r*ps_local_theta)/(ps_local_r) en los puntos iniciales
    # Para calcular los momentos iniciales locales, asumiremos que ps_local_r=1, ya que ademas, si estamos lejos del agujero negro,
    # ps_local_r es simplemente el modulo, determina la velocidad que tiene la partícula en la dirección radial
    # Hemos elegido ps_local_r positivo por qué estamos haciendo Backwards Ray Tracing

    ps_local_r=1
    ps_local_phi=(x*ps_local_r)/r_0 # Teóricamente debería de tener un menos, pero como la imagen la recibiriamos espejada, se debe añadir
    # otro menos para contrarestarlo, para mejorar la compación simplemente se ha puesto un unico signo +.
    ps_local_theta=(y*ps_local_r)/r_0

    # Con esto, podemos obtener los valores del cuatrimomento en las coordenadas de Boyer-Lindquist

    p_r_0= ps_local_r/Ar
    p_phi_0= ps_local_phi/Aphi 
    p_theta_0= ps_local_theta/Atheta
    p_t_0=mti.Mom_temp(*coords_0, p_r_0, p_phi_0, p_theta_0)

    tuple_momentos=(p_t_0, p_r_0, p_phi_0, p_theta_0) # Lista de los momentos en las coordenadas de Boyer-Lindquist
    return tuple_momentos 


def Screen_to_Momentum_Forwards(x:float, y:float)->tuple: # A diferencia del otro este arregla los menos de calcular la trayectoria hacia atrás en el tiempo

    coords_0=(t_0, r_0, phi_0, theta_0) # Tupla de coordenadas iniciales


    # Calculo de los parametros para obtener x e y, sigue la notacion de Chaotic Shadows
    At=math.sqrt((G(2, 2, *coords_0))/(G(2, 0, *coords_0)**2-G(0, 0, *coords_0)*G(2, 2, *coords_0)))
    Ar=1/math.sqrt(G(1, 1, *coords_0))
    Aphi=1/math.sqrt(G(2, 2, *coords_0))
    Atheta=1/math.sqrt(G(3, 3, *coords_0))
    Gamma=-((G(2, 0, *coords_0))/(G(2, 2, *coords_0)))*At  

    # Tenemos las siguientes dos ecuaciones: x=(-r*ps_local_phi)/(ps_local_r), y=(r*ps_local_theta)/(ps_local_r) en los puntos iniciales
    # Para calcular los momentos iniciales locales, asumiremos que ps_local_r=0.1, para resolver la geodesica suficientemente despacio
    # ps_local_r es simplemente el modulo, determina la velocidad que tiene la partícula en la dirección radial
    # Hemos elegido ps_local_r negativo por qué es la dirección de caida hacia el agujero negro (al contrario que en Backwards Ray-Tracing)

    ps_local_r=-0.1
    ps_local_phi=-(x*ps_local_r)/r_0 # Teóricamente debería de tener un menos, a diferencia del caso de generar una imagen no lo
                                     #recibimos espejado por lo que lo escribimos explícitamente.
    ps_local_theta=(y*ps_local_r)/r_0

    # Con esto, podemos obtener los valores del cuatrimomento en las coordenadas de Boyer-Lindquist

    p_r_0= ps_local_r/Ar
    p_phi_0= ps_local_phi/Aphi 
    p_theta_0= ps_local_theta/Atheta
    p_t_0=mti.Mom_temp_massive(*coords_0, p_r_0, p_phi_0, p_theta_0)

    tuple_momentos=(p_t_0, p_r_0, p_phi_0, p_theta_0) # Lista de los momentos en las coordenadas de Boyer-Lindquist
    return tuple_momentos 
