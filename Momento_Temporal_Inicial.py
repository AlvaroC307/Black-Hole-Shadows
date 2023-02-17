# Importar Librerias utiles
import numpy as np
import math

# Importar otros ficheros de la carpeta

import Function_Metric
from Function_Metric import *

# Solucionar la ecuación cuadrática general (Aplicado ya las simplificaciones de la metrica debidas a estar en Kerr(Mom_temp no simplificado))
# a*p_t^2+b*p_t+c, a=g^tt, b=2*g^{tphi}*p_phi, c=...
    
def Mom_temp(t,r,phi,theta,p_r,p_phi,p_theta,M,a):

    coord=(t, r, phi, theta)
    param=(M, a)
    A=Inv_G(0, 0, *coord, *param)
    B=2*(p_phi*Inv_G(0, 2, *coord, *param)+p_r*Inv_G(0, 1, *coord, *param)+p_theta*Inv_G(0, 3, *coord, *param))
    C1=p_r**2*Inv_G(1, 1, *coord, *param) +p_phi**2*Inv_G(2, 2, *coord, *param) +p_theta**2*Inv_G(3, 3, *coord, *param)
    C2=2*(p_r*p_phi*Inv_G(1, 2, *coord, *param)+p_r*p_theta*Inv_G(1, 3, *coord, *param)+p_phi*p_theta*Inv_G(2, 3, *coord, *param))
    C=C1+C2
    p_t_positivo=(-B+math.sqrt(B**2-4*A*C))/(2*A)
    
    if p_t_positivo<0:
        p_t=(-B-math.sqrt(B**2-4*A*C))/(2*A)
    else:
        p_t=p_t_positivo

    return p_t


def Mom_Sup_temp(t,r,phi,theta,ps_r,ps_phi,ps_theta,M,a):

    coord=(t, r, phi, theta)
    param=(M, a)
    A=G(0, 0, *coord, *param)
    B=2*ps_phi*G(0, 2, *coord, *param)
    C=ps_r**2*G(1, 1, *coord, *param) +ps_phi**2*G(2, 2, *coord, *param) +ps_theta**2*G(3, 3, *coord, *param)
    p_t_positivo=(-B+math.sqrt(B**2-4*A*C))/(2*A)
    
    if p_t_positivo<0:
        p_t=(-B-math.sqrt(B**2-4*A*C))/(2*A)
    else:
        p_t=p_t_positivo

    return p_t


# En este caso es para cambiar p^r, para ello, comprobamos el signo con el p^r calculado con el RK4
# Esta ecuacion es de la forma A*p^r**2+C=0, A=g_tt, C=...
def Mom_Sup_r(t,r,phi,theta,ps_t,ps_r,ps_phi,ps_theta,M,a):
    coord=(t, r, phi, theta)
    param=(M, a)
    A=G(1, 1, *coord, *param)
    C=ps_t**2*G(0, 0, *coord, *param) +ps_phi**2*G(2, 2, *coord, *param) +2*ps_phi*ps_t*G(0, 2, *coord, *param) +ps_theta**2*G(3, 3, *coord, *param)

    
    if (C/A>0):
        return "Imaginary"

    if ps_r<0:
        ps_r_final=-math.sqrt(-C/A)
    else:
        ps_r_final=math.sqrt(-C/A)

    return ps_r_final


# En este caso es para cambiar p^theta, para ello, comprobamos el signo con el p^theta calculado con el RK4
# Esta ecuacion es de la forma A*p^r**2+C=0, A=g_tt, C=...
def Mom_Sup_theta(t, r, phi, theta, ps_theta, M, a, E, L_z, Q):
    coords=(t, r, phi, theta)
    p_theta_cambio=math.sqrt(Q+(a*E*math.cos(theta))**2-(L_z/math.tan(theta))**2)

    ps_theta_cambio=Inv_G(3 , 3, *coords, M, a)*p_theta_cambio #AQUI YA SE UTILIZA QUE ES UN AGUJERO NEGRO DE KERR, PARA GENERALIZAR HAY QUE CAMBIAR PARTE DE ESTA FUNCION

    if ps_theta<0:
        ps_theta_final=-ps_theta_cambio
    else:
        ps_theta_final=ps_theta_cambio

    return ps_theta_final
