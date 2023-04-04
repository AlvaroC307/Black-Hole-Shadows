# Importar Librerias utiles
import math

# Importar otros ficheros de la carpeta
from Initial_Values import constantes
from Function_Metric import G, Inv_G

# Solucionar la ecuación cuadrática general (Aplicado ya las simplificaciones de la metrica debidas a estar en Kerr(Mom_temp no simplificado))
# a*p_t^2+b*p_t+c, a=g^tt, b=2*g^{tphi}*p_phi, c=...
    
def Mom_temp(t, r, phi, theta, p_r, p_phi, p_theta): # General

    coords=(t, r, phi, theta)

    # Parametros de la ecuacion de segundo grado
    A=Inv_G(0, 0, *coords)
    B=2*(p_phi*Inv_G(0, 2, *coords)+p_r*Inv_G(0, 1, *coords)+p_theta*Inv_G(0, 3, *coords))
    C1=p_r**2*Inv_G(1, 1, *coords) +p_phi**2*Inv_G(2, 2, *coords) +p_theta**2*Inv_G(3, 3, *coords)
    C2=2*(p_r*p_phi*Inv_G(1, 2, *coords)+p_r*p_theta*Inv_G(1, 3, *coords)+p_phi*p_theta*Inv_G(2, 3, *coords))
    C=C1+C2 # Suma de las funciones para obtener el parametro c
    p_t_positivo=(-B+math.sqrt(B**2-4*A*C))/(2*A) # Calculo de p_t con un mas antes de la raiz
    
    # Funcion if para que p_t sea siempre positivo y vaya en dirección futuro (el backwards se tiene en cuenta en las ecuaciones)
    if p_t_positivo<0:
        p_t=(-B-math.sqrt(B**2-4*A*C))/(2*A)
    else:
        p_t=p_t_positivo

    return p_t

""" 
def Mom_Sup_temp(t,r,phi,theta,ps_r,ps_phi,ps_theta,M,a): # Especifico de Kerr 

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

    return p_t """


# En este caso es para cambiar p^r, para ello, comprobamos el signo con el p^r calculado con el RK4
# Esta ecuacion es de la forma A*p^r**2+C=0, A=g_tt, C=...
def Mom_Sup_r(t, r, phi, theta, ps_t, ps_r, ps_phi, ps_theta): # ESPECIFICO DE TIPO KERR
    coords=(t, r, phi, theta)

    # Calculo de las constantes a,b,c para calcular p^r mediante la constante m^2=0
    A=G(1, 1, *coords)
    C=ps_t**2*G(0, 0, *coords) +ps_phi**2*G(2, 2, *coords) +2*ps_phi*ps_t*G(0, 2, *coords) +ps_theta**2*G(3, 3, *coords)

    # Si el valor es negativo dará un resultado imaginario, por lo que hay que decirselo a Solving_Kerr_with_Christoffel
    if (C/A>0):
        return "Imaginary"

    if ps_r<0: # Comprobación del signo de p^r obtenido mediante el RK4 para que eso se siga manteniendo
        ps_r_final=-math.sqrt(-C/A)
    else:
        ps_r_final=math.sqrt(-C/A)

    return ps_r_final



# ESTA ECUACIÓN REQUIERE DE LA EXISTENCIA DE LA CONSTANTE DE CARTER, POR LO QUE SE DEBE QUEDAR UNICAMENTE PARA KERR
# En este caso es para cambiar p^theta, para ello, comprobamos el signo con el p^theta calculado con el RK4
def Mom_Sup_theta(t, r, phi, theta, ps_theta, E, L_z, C): 
    coords=(t, r, phi, theta)
    
    # Calculo de p_theta mediante la constante de Carter
    p_theta_cambio=math.sqrt(C+(constantes['a']*E*math.cos(theta))**2-(L_z/math.tan(theta))**2) 
    # Cambio de p_theta a p^theta, ya que el programa utiliza p^mu
    ps_theta_cambio=Inv_G(3 , 3, *coords)*p_theta_cambio #AQUI YA SE UTILIZA QUE ES UN AGUJERO NEGRO DE KERR, PARA GENERALIZAR HAY QUE CAMBIAR PARTE DE ESTA FUNCION

    if ps_theta<0: # Comprobacion de que ps_theta sea del mismo signo que el dato obtenido mediante el RK4
        ps_theta_final=-ps_theta_cambio
    else:
        ps_theta_final=ps_theta_cambio

    return ps_theta_final
