# Importar Librerias utiles

import math
from math import sin
from math import cos
from math import tan

def Delta(r, M, a):
    return r**2+a**2-2*M*r


def rho2(r, theta, a):
    return r**2+(a*cos(theta))**2


def G(i,j,t,r,phi,theta,M,a):
    if i==0:
        if j==0:
            return -(1-(2*M*r)/(rho2(r, theta, a)))
        elif j==1:
            return 0
        elif j==2:
            return -(2*M*r*a*(sin(theta))**2)/(rho2(r, theta, a))
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
            return -(2*M*r*a*(sin(theta))**2)/(rho2(r, theta, a))
        elif j==1:
            return 0
        elif j==2:
            frac_g22=(2*M*r*(a*sin(theta))**2)/(rho2(r, theta, a))
            return ((r**2+a**2+frac_g22))*(sin(theta))**2
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
            sum2=2*M*r*(a*sin(theta))**2
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
            return (Delta(r, M, a)-(a*sin(theta))**2)/(rho2(r, theta, a)*Delta(r, M, a)*(sin(theta))**2)
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


# i hace referencia al superindice, j y k son los subindices

def Christoffel(i,j,k,t,r,phi,theta,M,a):
    if i==0:
        if j==0:
            if k==0:
                return 0
            if k==1:
                return 1.0*M*(a**2 + r**2)*(-a**2*cos(theta)**2 + r**2)/((a**2*cos(theta)**2 + r**2)**2*(-2*M*r + a**2 + r**2))
            if k==2:
                return 0
            if k==3:
                return M*a**2*r*(-4.0*M*a**2*r*sin(theta)**2 + 4.0*M*r*(a**2 + r**2) - 2.0*(a**2 + r**2)*(a**2*cos(theta)**2 + r**2))*sin(theta)*cos(theta)/((a**2*cos(theta)**2 + r**2)**3*(-2*M*r + a**2 + r**2))
        if j==1:
            if k==0:
                return 1.0*M*(a**2 + r**2)*(-a**2*cos(theta)**2 + r**2)/((a**2*cos(theta)**2 + r**2)**2*(-2*M*r + a**2 + r**2))
            if k==1:
                return 0
            if k==2:
                return M*a*(1.0*a**6*cos(theta)**4 - 1.0*a**4*r**2*cos(theta)**4 - 4.0*a**2*r**4*cos(theta)**2 - 1.0*a**2*r**4 - 3.0*r**6)*sin(theta)**2/((a**2*cos(theta)**2 + r**2)**3*(-2*M*r + a**2 + r**2))
            if k==3:
                return 0
        if j==2:
            if k==0:
                return 0
            if k==1:
                return M*a*(1.0*a**6*cos(theta)**4 - 1.0*a**4*r**2*cos(theta)**4 - 4.0*a**2*r**4*cos(theta)**2 - 1.0*a**2*r**4 - 3.0*r**6)*sin(theta)**2/((a**2*cos(theta)**2 + r**2)**3*(-2*M*r + a**2 + r**2))
            if k==2:
                return 0
            if k==3:
                return 2.0*M*a**3*r*sin(theta)**3*cos(theta)/(1.0*a**4*cos(theta)**4 + 2.0*a**2*r**2*cos(theta)**2 + 1.0*r**4)
        if j==3:
            if k==0:
                return M*a**2*r*(-4.0*M*a**2*r*sin(theta)**2 + 4.0*M*r*(a**2 + r**2) - 2.0*(a**2 + r**2)*(a**2*cos(theta)**2 + r**2))*sin(theta)*cos(theta)/((a**2*cos(theta)**2 + r**2)**3*(-2*M*r + a**2 + r**2))
            if k==1:
                return 0
            if k==2:
                return 2.0*M*a**3*r*sin(theta)**3*cos(theta)/(1.0*a**4*cos(theta)**4 + 2.0*a**2*r**2*cos(theta)**2 + 1.0*r**4)
            if k==3:
                return 0
    if i==1:
        if j==0:
            if k==0:
                return 1.0*M*(-a**2*cos(theta)**2 + r**2)*(-2*M*r + a**2 + r**2)/(a**2*cos(theta)**2 + r**2)**3 
            if k==1:
                return 0
            if k==2:
                return 1.0*M*a*(a**2*cos(theta)**2 - r**2)*(-2*M*r + a**2 + r**2)*sin(theta)**2/(a**2*cos(theta)**2 + r**2)**3
            if k==3:
                return 0
        if j==1:
            if k==0:
                return 0
            if k==1:
                return (1.0*r*(-2*M*r + a**2 + r**2) + (M - r)*(a**2*cos(theta)**2 + r**2))/((a**2*cos(theta)**2 + r**2)*(-2*M*r + a**2 + r**2))
            if k==2:
                return 0
            if k==3:
                return -1.0*a**2*sin(2*theta)/(a**2*cos(2*theta) + a**2 + 2*r**2)
        if j==2:
            if k==0:
                return 1.0*M*a*(a**2*cos(theta)**2 - r**2)*(-2*M*r + a**2 + r**2)*sin(theta)**2/(a**2*cos(theta)**2 + r**2)**3
            if k==1:
                return 0
            if k==2:
                return (2.0*M*r - 1.0*a**2 - 1.0*r**2)*(-2*M*a**2*r**2*sin(theta)**2 + M*a**2*(a**2*cos(theta)**2 + r**2)*sin(theta)**2 + r*(a**2*cos(theta)**2 + r**2)**2)*sin(theta)**2/(a**2*cos(theta)**2 + r**2)**3
            if k==3:
                return 0
        if j==3:
            if k==0:
                return 0
            if k==1:
                return -1.0*a**2*sin(2*theta)/(a**2*cos(2*theta) + a**2 + 2*r**2)
            if k==2:
                return 0
            if k==3:
                return -1.0*r*(-2*M*r + a**2 + r**2)/(a**2*cos(theta)**2 + r**2)
    if i==2:
        if j==0:
            if k==0:
                return 0
            if k==1:
                return 1.0*M*a*(-a**2*cos(theta)**2 + r**2)/((a**2*cos(theta)**2 + r**2)**2*(-2*M*r + a**2 + r**2))
            if k==2:
                return 0
            if k==3:
                return M*a*r*(-4.0*M*a**2*r*sin(theta)**2 + 2.0*(a**2 + r**2)*(2*M*r - a**2*cos(theta)**2 - r**2))/((a**2*cos(theta)**2 + r**2)**3*(-2*M*r + a**2 + r**2)*tan(theta))
        if j==1:
            if k==0:
                return 1.0*M*a*(-a**2*cos(theta)**2 + r**2)/((a**2*cos(theta)**2 + r**2)**2*(-2*M*r + a**2 + r**2))
            if k==1:
                return 0
            if k==2:
                return (-1.0*M*a**4*(1 - cos(theta)**2)**2 - 1.0*M*a**4*cos(theta)**2 + 1.0*M*a**4 - 1.0*M*a**2*r**2*cos(theta)**2 - 1.0*M*a**2*r**2 - 2.0*M*r**4 + 1.0*a**4*r*(1 - cos(theta)**2)**2 + 2.0*a**4*r*cos(theta)**2 - 1.0*a**4*r + 2.0*a**2*r**3*cos(theta)**2 + 1.0*r**5)/((a**2*cos(theta)**2 + r**2)**2*(-2*M*r + a**2 + r**2))
            if k==3:
                return 0
        if j==2:
            if k==0:
                return 0
            if k==1:
                return (-1.0*M*a**4*(1 - cos(theta)**2)**2 - 1.0*M*a**4*cos(theta)**2 + 1.0*M*a**4 - 1.0*M*a**2*r**2*cos(theta)**2 - 1.0*M*a**2*r**2 - 2.0*M*r**4 + 1.0*a**4*r*(1 - cos(theta)**2)**2 + 2.0*a**4*r*cos(theta)**2 - 1.0*a**4*r + 2.0*a**2*r**3*cos(theta)**2 + 1.0*r**5)/((a**2*cos(theta)**2 + r**2)**2*(-2*M*r + a**2 + r**2))
            if k==2:
                return 0
            if k==3:
                return (4.0*M**2*a**2*r**2*(a**2 + r**2)*sin(theta)**2 - 1.0*(2*M*a**2*r*(a**2 + r**2)*sin(theta)**2 + (a**2*cos(theta)**2 + r**2)*(2*M*a**2*r*sin(theta)**2 + (a**2 + r**2)*(a**2*cos(theta)**2 + r**2)))*(2*M*r - a**2*cos(theta)**2 - r**2))/((a**2*cos(theta)**2 + r**2)**3*(-2*M*r + a**2 + r**2)*tan(theta))
        if j==3:
            if k==0:
                return M*a*r*(-4.0*M*a**2*r*sin(theta)**2 + 2.0*(a**2 + r**2)*(2*M*r - a**2*cos(theta)**2 - r**2))/((a**2*cos(theta)**2 + r**2)**3*(-2*M*r + a**2 + r**2)*tan(theta))
            if k==1:
                return 0
            if k==2:
                return (4.0*M**2*a**2*r**2*(a**2 + r**2)*sin(theta)**2 - 1.0*(2*M*a**2*r*(a**2 + r**2)*sin(theta)**2 + (a**2*cos(theta)**2 + r**2)*(2*M*a**2*r*sin(theta)**2 + (a**2 + r**2)*(a**2*cos(theta)**2 + r**2)))*(2*M*r - a**2*cos(theta)**2 - r**2))/((a**2*cos(theta)**2 + r**2)**3*(-2*M*r + a**2 + r**2)*tan(theta))
            if k==3:
                return 0
    if i==3:
        if j==0:
            if k==0:
                return -8.0*M*a**2*r*sin(2*theta)/(a**2*cos(2*theta) + a**2 + 2*r**2)**3
            if k==1:
                return 0
            if k==2:
                return 8.0*M*a*r*(a**2 + r**2)*sin(2*theta)/(a**2*cos(2*theta) + a**2 + 2*r**2)**3
            if k==3:
                return 0
        if j==1:
            if k==0:
                return 0
            if k==1:
                return 1.0*a**2*sin(2*theta)/((-2*M*r + a**2 + r**2)*(a**2*cos(2*theta) + a**2 + 2*r**2))
            if k==2:
                return 0
            if k==3:
                return 1.0*r/(a**2*cos(theta)**2 + r**2) 
        if j==2:
            if k==0:
                return 8.0*M*a*r*(a**2 + r**2)*sin(2*theta)/(a**2*cos(2*theta) + a**2 + 2*r**2)**3
            if k==1:
                return 0
            if k==2:
                return (-2.0*M*a**2*r*(a**2 + r**2)*sin(theta)**2 - 1.0*(a**2*cos(theta)**2 + r**2)*(2*M*a**2*r*sin(theta)**2 + (a**2 + r**2)*(a**2*cos(theta)**2 + r**2)))*sin(theta)*cos(theta)/(a**2*cos(theta)**2 + r**2)**3
            if k==3:
                return 0
        if j==3:
            if k==0:
                return 0
            if k==1:
                return 1.0*r/(a**2*cos(theta)**2 + r**2)
            if k==2:
                return 0
            if k==3:
                return -1.0*a**2*sin(2*theta)/(a**2*cos(2*theta) + a**2 + 2*r**2)