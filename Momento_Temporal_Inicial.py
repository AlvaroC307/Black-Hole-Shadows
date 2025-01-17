# Importar Librerias utiles
import math

# Importar otros ficheros de la carpeta
from Initial_Values import constantes, m_Geo
from Function_Metric import G, Inv_G

# Solucionar la ecuación cuadrática general (Aplicado ya las simplificaciones de la metrica debidas a estar en Kerr(Mom_temp no simplificado))
# a*p_t^2+b*p_t+c, a=g^tt, b=2*g^{tphi}*p_phi, c=...
    
def Mom_temp(t:float, r:float, phi:float, theta:float, p_r:float, p_phi:float, p_theta:float)->float: # General

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

# ESTA FUNCION TIENE EN CUENTA POSIBILIDAD DE PARTÍCULAS MASIVAS. ES MÁS GENERAL QUE LA ANTERIOR PERO ES LIGERAMENTE MÁS LENTA
# Solucionar la ecuación cuadrática general a*p_t^2+b*p_t+c=0, a=g^tt, b=2*(g^{tphi}*p_phi+g^{tr}*p_r+g^{ttheta}*p_theta), c=...
    
def Mom_temp_massive(t:float, r:float, phi:float, theta:float, p_r:float, p_phi:float, p_theta:float)->float|list: # General

    coords=(t, r, phi, theta)

    # Parametros de la ecuacion de segundo grado
    A=Inv_G(0, 0, *coords)
    B=2*(p_phi*Inv_G(0, 2, *coords)+p_r*Inv_G(0, 1, *coords)+p_theta*Inv_G(0, 3, *coords))
    C1=p_r**2*Inv_G(1, 1, *coords) +p_phi**2*Inv_G(2, 2, *coords) +p_theta**2*Inv_G(3, 3, *coords)
    C2=2*(p_r*p_phi*Inv_G(1, 2, *coords)+p_r*p_theta*Inv_G(1, 3, *coords)+p_phi*p_theta*Inv_G(2, 3, *coords))
    C=C1+C2+m_Geo**2 # Suma de las funciones para obtener el parametro c
    p_t_positivo=(-B+math.sqrt(B**2-4*A*C))/(2*A) # Calculo de p_t con un mas antes de la raiz
    
    # Funcion if para que p_t sea siempre positivo y vaya en dirección futuro (el backwards se tiene en cuenta en las ecuaciones)
    if p_t_positivo<0:
        p_t=(-B-math.sqrt(B**2-4*A*C))/(2*A)
    else:
        p_t=p_t_positivo

    return p_t


# En este caso es para cambiar p^r, para ello, comprobamos el signo con el p^r calculado con el RK4
# Esta ecuacion es de la forma A*p^r**2+C=0, A=g_tt, C=...
def Mom_Sup_r(ps_t:float, ps_r:float, ps_phi:float, ps_theta:float, coords:tuple)->float|str: # ESPECIFICO DE TIPO KERR
    
    # Calculo de las constantes a,b,c para calcular p^r mediante la constante m^2=0
    A=G(1, 1, *coords)
    B=2*(ps_t*G(1, 0, *coords)+ps_phi*G(1, 2, *coords)+ps_theta*G(1, 3, *coords))
    C1=ps_t**2*G(0, 0, *coords) +ps_phi**2*G(2, 2, *coords) +ps_theta**2*G(3, 3, *coords)
    C2=2*(ps_phi*ps_t*G(0, 2, *coords)+2*ps_t*ps_theta*G(0, 3, *coords)+2*ps_phi*ps_theta*G(2, 3, *coords))
    C=C1+C2

    # Si el valor es negativo dará un resultado imaginario, por lo que hay que decirselo a Solving_Kerr_with_Christoffel
    Discriminante=B**2-4*A*C
    if (Discriminante<0):
        return "Imaginary"

    ps_r_cambio_positivo=(-B+math.sqrt(Discriminante))/(2*A)
    ps_r_cambio_negativo=(-B-math.sqrt(Discriminante))/(2*A)


    if ps_r>0: # Comprobación del signo de p^r obtenido mediante el RK4 para que eso se siga manteniendo
        if ps_r_cambio_negativo>0:
            return ps_r_cambio_negativo
        else:
            return ps_r_cambio_positivo
    else:
        if ps_r_cambio_positivo<0:
            return ps_r_cambio_positivo
        else:
            return ps_r_cambio_negativo




# ESTA ECUACIÓN REQUIERE DE LA EXISTENCIA DE LA CONSTANTE DE CARTER, POR LO QUE SE DEBE QUEDAR UNICAMENTE PARA KERR
# En este caso es para cambiar p^theta, para ello, comprobamos el signo con el p^theta calculado con el RK4
def Mom_Sup_theta(t:float, r:float, phi:float, theta:float, ps_theta:float, E:float, L_z:float, C:float)->float|str: 
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
