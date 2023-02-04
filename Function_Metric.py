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


list_Metric=[]
list_Inv_Metric=[]
for row in Reader_Metric:
    content = row[2]
    list_Metric.append(content)


for row in Reader_Inv_Metric:
    content = row[2]
    list_Inv_Metric.append(content)

csv_Metric.close()
csv_Inv_Metric.close()


# Eso era para la lectura de Metric y Inverse Metric, ahora toca Christoffel symbols 
list_Chris=[]
csv_Chris= open('./Data/Christoffel_symbols.csv', 'r')
Reader_Chris = csv.reader(csv_Chris)

for row in Reader_Chris:
    content = row[3]
    list_Chris.append(content)


csv_Chris.close()

#-------------------Definicion de las funciones Metric, Inverse Metric y Christoffel Symbols 

def G(i,j,t,r,phi,theta,M,a):
    if i==0:
        if j==0:
            return eval(list_Metric[0])
        elif j==1:
            return eval(list_Metric[1])
        elif j==2:
            return eval(list_Metric[2])
        elif j==3:
            return eval(list_Metric[3])
    if i==1:
        if j==0:
            return eval(list_Metric[4])
        elif j==1:
            return eval(list_Metric[5])
        elif j==2:
            return eval(list_Metric[6])
        elif j==3:
            return eval(list_Metric[7])
    if i==2:
        if j==0:
            return eval(list_Metric[8])
        elif j==1:
            return eval(list_Metric[9])
        elif j==2:
            return eval(list_Metric[10])
        elif j==3:
            return eval(list_Metric[11])
    if i==3:
        if j==0:
            return eval(list_Metric[12])
        elif j==1:
            return eval(list_Metric[13])
        elif j==2:
            return eval(list_Metric[14])
        elif j==3:
            return eval(list_Metric[15])


def Inv_G(i,j,t,r,phi,theta,M,a):
    if i==0:
        if j==0:
            return eval(list_Inv_Metric[0])
        elif j==1:
            return eval(list_Inv_Metric[1])
        elif j==2:
            return eval(list_Inv_Metric[2])
        elif j==3:
            return eval(list_Inv_Metric[3])
    if i==1:
        if j==0:
            return eval(list_Inv_Metric[4])
        elif j==1:
            return eval(list_Inv_Metric[5])
        elif j==2:
            return eval(list_Inv_Metric[6])
        elif j==3:
            return eval(list_Inv_Metric[7])
    if i==2:
        if j==0:
            return eval(list_Inv_Metric[8])
        elif j==1:
            return eval(list_Inv_Metric[9])
        elif j==2:
            return eval(list_Inv_Metric[10])
        elif j==3:
            return eval(list_Inv_Metric[11])
    if i==3:
        if j==0:
            return eval(list_Inv_Metric[12])
        elif j==1:
            return eval(list_Inv_Metric[13])
        elif j==2:
            return eval(list_Inv_Metric[14])
        elif j==3:
            return eval(list_Inv_Metric[15])



# i hace referencia al superindice, j y k son los subindices

def Christoffel(i,j,k,t,r,phi,theta,M,a):
    if i==0:
        if j==0:
            if k==0:
                return eval(list_Chris[0])
            if k==1: 
                return eval(list_Chris[1])
            if k==2:
                return eval(list_Chris[2])
            if k==3:
                return eval(list_Chris[3])
        if j==1:
            if k==0:
                return eval(list_Chris[4])
            if k==1:
                return eval(list_Chris[5])
            if k==2:
                return eval(list_Chris[6])
            if k==3:
                return eval(list_Chris[7])
        if j==2:
            if k==0:
                return eval(list_Chris[8])
            if k==1:
                return eval(list_Chris[9])
            if k==2:
                return eval(list_Chris[10])
            if k==3:
                return eval(list_Chris[11])
        if j==3:
            if k==0:
                return eval(list_Chris[12])
            if k==1:
                return eval(list_Chris[13])
            if k==2:
                return eval(list_Chris[14])
            if k==3:
                return eval(list_Chris[15])
    if i==1:
        if j==0:
            if k==0:
                return eval(list_Chris[16])
            if k==1:
                return eval(list_Chris[17])
            if k==2:
                return eval(list_Chris[18])
            if k==3:
                return eval(list_Chris[19])
        if j==1:
            if k==0:
                return eval(list_Chris[20])
            if k==1:
                return eval(list_Chris[21])
            if k==2:
                return eval(list_Chris[22])
            if k==3:
                return eval(list_Chris[23])
        if j==2:
            if k==0:
                return eval(list_Chris[24])
            if k==1:
                return eval(list_Chris[25])
            if k==2:
                return eval(list_Chris[26])
            if k==3:
                return eval(list_Chris[27])
        if j==3:
            if k==0:
                return eval(list_Chris[28])
            if k==1:
                return eval(list_Chris[29])
            if k==2:
                return eval(list_Chris[30])
            if k==3:
                return eval(list_Chris[31])
    if i==2:
        if j==0:
            if k==0:
                return eval(list_Chris[32])
            if k==1:
                return eval(list_Chris[33])
            if k==2:
                return eval(list_Chris[34])
            if k==3:
                return eval(list_Chris[35])
        if j==1:
            if k==0:
                return eval(list_Chris[36])
            if k==1:
                return eval(list_Chris[37])
            if k==2:
                return eval(list_Chris[38])
            if k==3:
                return eval(list_Chris[39])
        if j==2:
            if k==0:
                return eval(list_Chris[40])
            if k==1:
                return eval(list_Chris[41])
            if k==2:
                return eval(list_Chris[42])
            if k==3:
                return eval(list_Chris[43])
        if j==3:
            if k==0:
                return eval(list_Chris[44])
            if k==1:
                return eval(list_Chris[45])
            if k==2:
                return eval(list_Chris[46])
            if k==3:
                return eval(list_Chris[47])
    if i==3:
        if j==0:
            if k==0:
                return eval(list_Chris[48])
            if k==1:
                return eval(list_Chris[49])
            if k==2:
                return eval(list_Chris[50])
            if k==3:
                return eval(list_Chris[51])
        if j==1:
            if k==0:
                return eval(list_Chris[52])
            if k==1:
                return eval(list_Chris[53])
            if k==2:
                return eval(list_Chris[54])
            if k==3:
                return eval(list_Chris[55])
        if j==2:
            if k==0:
                return eval(list_Chris[56])
            if k==1:
                return eval(list_Chris[57])
            if k==2:
                return eval(list_Chris[58])
            if k==3:
                return eval(list_Chris[59])
        if j==3:
            if k==0:
                return eval(list_Chris[60])
            if k==1:
                return eval(list_Chris[61])
            if k==2:
                return eval(list_Chris[62])
            if k==3:
                return eval(list_Chris[63])