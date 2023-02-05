# Importar Librerias utiles

import math
from math import *
import csv
import Function_Metric
from Function_Metric import *



file_manager=open('./Data/Christoffel_prueba_cambio.csv', "w", newline="")
csvfile = csv.writer(file_manager)

M=1
a=0.9
r_0 = (1.4358)*M
theta_0 = math.pi/3
phi_0 = 0
t_0 = 0

for i in range(4):
    for j in range(4):
        for k in range(4):
            Chris_ijk=Christoffel(i,j,k,t_0,r_0,phi_0,theta_0,M,a)
            print("Progreso: [",i,j,k,"]")
            csvfile.writerow([i,j,k,Chris_ijk])


file_manager.close()

