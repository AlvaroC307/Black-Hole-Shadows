# Importar Librerias utiles

import math
from math import *
import csv


# Definiciones de las funciones Delta y rho^2
def Delta(r, M, a):
    return r**2+a**2-2*M*r


def rho2(r, theta, a):
    return r**2+(a*cos(theta))**2


# Lectura de los ficheros Metric, Inverse_Metric y Christoffel_symbols

csv_Metric= open('./Data/Metric.csv', 'r')
Reader_Metric = csv.reader(csv_Metric)
csv_Inv_Metric= open('./Data/Inverse_Metric.csv', 'r')
Reader_Inv_Metric = csv.reader(csv_Inv_Metric)


n=0
list_Metric=[]
Matrix_Metric=[]

for row in Reader_Metric:
    content = row[2]
    list_Metric.append(content)
    n+=1
    if n==4:
        Matrix_Metric.append(list_Metric)
        list_Metric=[]
        n=0


n=0
list_Inv_Metric=[]
Matrix_Inv_Metric=[]

for row in Reader_Inv_Metric:
    content = row[2]
    list_Inv_Metric.append(content)
    n+=1
    if n==4:
        Matrix_Inv_Metric.append(list_Inv_Metric)
        list_Inv_Metric=[]
        n=0

csv_Metric.close()
csv_Inv_Metric.close()


# Eso era para la lectura de Metric y Inverse Metric, ahora toca Christoffel symbols 

csv_Chris= open('./Data/Christoffel_symbols.csv', 'r')
Reader_Chris = csv.reader(csv_Chris)


n=0
m=0
list_Chris=[]
Matrix_Chris=[]
Tri_Matrix_Chris=[]
for row in Reader_Chris:
    content = row[3]
    list_Chris.append(content)
    n+=1
    if n==4:
        Matrix_Chris.append(list_Chris)
        list_Chris=[]
        n=0
        m+=1
        if m==4:
            Tri_Matrix_Chris.append(Matrix_Chris)
            Matrix_Chris=[]
            m=0


csv_Chris.close()

#-------------------Definicion de las funciones Metric, Inverse Metric y Christoffel Symbols 

def G(i,j,t,r,phi,theta,M,a):
    return eval(Matrix_Metric[i][j])


def Inv_G(i,j,t,r,phi,theta,M,a):
    return eval(Matrix_Inv_Metric[i][j])


# i hace referencia al superindice, j y k son los subindices

def Christoffel(i,j,k,t,r,phi,theta,M,a):
    return eval(Tri_Matrix_Chris[i][j][k])
