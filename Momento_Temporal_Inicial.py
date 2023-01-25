# Importar Librerias utiles
import numpy as np
import math

# Importar otros ficheros de la carpeta

import Function_Metric
from Function_Metric import *

# Solucionar la ecuación cuadrática general (Aplicado ya las simplificaciones de la metrica debidas a estar en Kerr)
# a*p_t^2+b*p_t+c, a=g^tt, b=2*g^{tphi}*p_phi, c=...
    
def Mom_temp(t,r,phi,theta,p_r,p_theta,p_phi,M,a):

    coord=(t,r,phi,theta)
    param=(M,a)
    A=Inv_G(0,0,*coord,*param)
    B=2*p_phi*Inv_G(0,2,*coord,*param)
    C=p_r**2*Inv_G(1,1,*coord,*param) +p_phi**2*Inv_G(2,2,*coord,*param) +p_theta**2*Inv_G(3,3,*coord,*param)
    p_t_positivo=(-B+math.sqrt(B**2-4*A*C))/(2*A)
    
    if p_t_positivo<0:
        p_t=(-B-math.sqrt(B**2-4*A*C))/(2*A)
    else:
        p_t=p_t_positivo

    return p_t

def Mom_Sup_r(t,r,phi,theta,p_t,p_theta,p_phi,M,a):
    coord=(t,r,phi,theta)
    param=(M,a)
    
