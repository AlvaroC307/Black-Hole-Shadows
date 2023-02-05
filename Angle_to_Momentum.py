# Importar ficheros útiles
import math
import Function_Metric
from Function_Metric import *
import Momento_Temporal_Inicial as mti

# Ahora mismo será especifico a un agujero negro tipo Kerr, es decir: métrica diagonal excepto en los términos t-phi
# la matriz de transformación de la base del observador a la base coordenadas, calculamos los 5 elementos primero

def Screen_to_Momentum(x, y, t_0, r_0, phi_0, theta_0, M, a):

    coords_0=(t_0, r_0, phi_0, theta_0)
    param=(M, a)

    At=math.sqrt((G(2, 2, *coords_0, *param))/(G(2, 0, *coords_0, *param)**2-G(0, 0, *coords_0, *param)*G(2, 2, *coords_0, *param)))
    Ar=1/math.sqrt(G(1, 1, *coords_0, *param))
    Aphi=1/math.sqrt(G(2, 2, *coords_0, *param))
    Atheta=1/math.sqrt(G(3, 3, *coords_0, *param))
    Gamma=-((G(2, 0, *coords_0, *param))/(G(2, 2, *coords_0, *param)))*At  

    # Tenemos las siguientes dos ecuaciones: x=(-r*ps_local_phi)/(ps_local_r), y=(r*ps_local_theta)/(ps_local_r) en los puntos iniciales
    # Para calcular los momentos iniciales locales, asumiremos que ps_local_r=1, ya que ademas, si estamos lejos del agujero negro,
    # ps_local_r es simplemente el modulo, el cual no tendrá importancia en el cálculo de la forma de la sombra

    ps_local_r=1
    ps_local_phi=-(x*ps_local_r)/r_0
    ps_local_theta=(y*ps_local_r)/r_0

    # Con esto, podemos obtener los valores del cuatrimomento en las coordenadas de Boyer-Lindquist

    p_r_0= ps_local_r/Ar
    p_phi_0= ps_local_phi/Aphi
    p_theta_0= ps_local_theta/Atheta
    p_t_0=mti.Mom_temp(*coords_0,p_r_0,p_phi_0,p_theta_0,*param)

    list_momentos=[p_t_0, p_r_0, p_phi_0, p_theta_0]
    return list_momentos


# Para hacer pruebas
x, y = 0 ,0
M, a=1, 0 
t_0, r_0, phi_0, theta_0=0, 5*M, 0, math.pi/2

coords_0=(t_0, r_0, phi_0, theta_0)
param=(M, a)

print(Screen_to_Momentum(x,y,*coords_0,*param))