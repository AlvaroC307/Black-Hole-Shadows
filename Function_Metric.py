# Importar Librerias utiles

import math

def Delta(r, M, a):
    return r**2+a**2-2*M*r


def rho2(r, theta, a):
    return r**2+(a*math.cos(theta))**2


def G(i,j,t,r,phi,theta,M,a):
    if i==0:
        if j==0:
            return -(1-(2*M*r)/(rho2(r, theta, a)))
        elif j==1:
            return 0
        elif j==2:
            return -(2*M*r*a*(math.sin(theta))**2)/(rho2(r, theta, a))
        elif j==3:
            return 0
    if i==1:
        if j==0:
            return 0
        elif j==1:
            return (rho2(r, theta, a))/(Delta(r, M, a))
        elif j==2:
            return 0
        elif j==3:
            return 0
    if i==2:
        if j==0:
            return -(2*M*r*a*(math.sin(theta))**2)/(rho2(r, theta, a))
        elif j==1:
            return 0
        elif j==2:
            frac_g22=(2*M*r*(a*math.sin(theta))**2)/(rho2(r, theta, a))
            return ((r**2+a**2+frac_g22))*(math.sin(theta))**2
        elif j==3:
            return 0
    if i==3:
        if j==0:
            return 0
        elif j==1:
            return 0
        elif j==2:
            return 0
        elif j==3:
            return rho2(r, theta, a)


def Inv_G(i,j,t,r,phi,theta,M,a):
    if i==0:
        if j==0:
            sum1=(r**2+a**2)*rho2(r, theta, a)
            sum2=2*M*r*(a*math.sin(theta))**2
            return -(sum1+sum2)/(rho2(r, theta, a)*Delta(r, M, a))
        elif j==1:
            return 0
        elif j==2:
            return -(2*M*r*a)/(rho2(r, theta, a)*Delta(r, M, a))
        elif j==3:
            return 0
    if i==1:
        if j==0:
            return 0
        elif j==1:
            return (Delta(r, M, a))/(rho2(r, theta, a))
        elif j==2:
            return 0
        elif j==3:
            return 0
    if i==2:
        if j==0:
            return -(2*M*r*a)/(rho2(r, theta, a)*Delta(r, M, a))
        elif j==1:
            return 0
        elif j==2:
            return (Delta(r, M, a)-(a*math.sin(theta))**2)/(rho2(r, theta, a)*Delta(r, M, a)*(math.sin(theta))**2)
        elif j==3:
            return 0
    if i==3:
        if j==0:
            return 0
        elif j==1:
            return 0
        elif j==2:
            return 0
        elif j==3:
            return 1/rho2(r, theta, a)
