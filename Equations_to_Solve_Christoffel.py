# Importar otros ficheros de la carpeta

from Function_Metric import *

# Definir las 8 funciones que se van a integrar con los simbolos de christoffel

# la ecuacion de la geodesica dot(x^mu)=p^mu
# ps_x significa p^x

def t_punto(ps_t):
    return ps_t


def r_punto(ps_r):
    return ps_r


def phi_punto(ps_phi):
    return ps_phi


def theta_punto(ps_theta):
    return ps_theta


# la ecuacion seria: dot(p^mu)=-sum(p^alpha*sum(p^beta*chris(mu,alpha,beta))), la ecuacion de la geodesica donde dot(x^mu)=p^mu

def ps_t_punto(t, r, phi, theta, ps_t, ps_r, ps_phi, ps_theta, M, a):
    coords=(t,r,phi,theta)
    param=(M, a)
    moms=[ps_t, ps_r, ps_phi, ps_theta]
    suma_alpha=0
    for alpha in range(4):
        suma_beta=0
        for beta in range(4):
            suma_beta+=(moms[beta]*Christoffel(0, alpha, beta, *coords, *param))
        suma_alpha+=(moms[alpha]*suma_beta)
    return -suma_alpha


def ps_r_punto(t, r, phi, theta, ps_t, ps_r, ps_phi, ps_theta, M, a):
    coords=(t,r,phi,theta)
    param=(M, a)
    moms=[ps_t, ps_r, ps_phi, ps_theta]
    suma_alpha=0
    for alpha in range(4):
        suma_beta=0
        for beta in range(4):
            suma_beta+=(moms[beta]*Christoffel(1, alpha, beta, *coords, *param))
        suma_alpha+=(moms[alpha]*suma_beta)
    return -suma_alpha


def ps_phi_punto(t, r, phi, theta, ps_t, ps_r, ps_phi, ps_theta, M, a):
    coords=(t,r,phi,theta)
    param=(M, a)
    moms=[ps_t, ps_r, ps_phi, ps_theta]
    suma_alpha=0
    for alpha in range(4):
        suma_beta=0
        for beta in range(4):
            suma_beta+=(moms[beta]*Christoffel(2, alpha, beta, *coords, *param))
        suma_alpha+=(moms[alpha]*suma_beta)
    return -suma_alpha


def ps_theta_punto(t, r, phi, theta, ps_t, ps_r, ps_phi, ps_theta, M, a):
    coords=(t,r,phi,theta)
    param=(M, a)
    moms=[ps_t, ps_r, ps_phi, ps_theta]
    suma_alpha=0
    for alpha in range(4):
        suma_beta=0
        for beta in range(4):
            suma_beta+=(moms[beta]*Christoffel(3, alpha, beta, *coords, *param))
        suma_alpha+=(moms[alpha]*suma_beta)
    return -suma_alpha


# El menos se debe a que estamos integrando la ecuacion hacia atras en la curva geodesica, por lo que se añade un menos al parámetro

def Switch_punto(i, t, r, phi, theta, ps_t, ps_r, ps_phi, ps_theta, M, a):
    if i == 0:
        return -ps_t_punto(t, r, phi, theta, ps_t, ps_r, ps_phi, ps_theta, M, a)
    elif i == 1:
        return -ps_r_punto(t, r, phi, theta, ps_t, ps_r, ps_phi, ps_theta, M, a)
    elif i == 2:
        return -ps_phi_punto(t, r, phi, theta, ps_t, ps_r, ps_phi, ps_theta, M, a)
    elif i == 3:
        return -ps_theta_punto(t, r, phi, theta, ps_t, ps_r, ps_phi, ps_theta, M, a)
    elif i == 4:
        return -t_punto(ps_t)
    elif i == 5:
        return -r_punto(ps_r)
    elif i==6:
        return -phi_punto(ps_phi)
    elif i==7:
        return -theta_punto(ps_theta)