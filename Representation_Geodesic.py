import matplotlib.pyplot as plt
import csv
import math
import numpy as np
from Initial_Values import M, constantes, phi_0_Geo, name

def r_Horizon():

    if name=="Schwarzschild":
        r_Horizon=2*M
    if name=="Kerr":
        r_Horizon=M+math.sqrt(M**2-constantes["a"]**2)
    elif name=="Kerr_Newman":
        r_Horizon=M+math.sqrt(M**2-constantes["a"]**2-constantes["Q_e"]**2)

    return r_Horizon


def plot_tr(): # Funcion para la grafica (r/M, t/M), hemos tomado c=1. 

    graf_name="t frente a r"
    r_mas=r_Horizon()

    csv_file= open('./Data/Specific_Geodesic.csv', 'r') #Leer el fichero de los datos de la geodesica
    Reader_file = csv.reader(csv_file)

    list_t=[]
    list_r=[] 
    list_r_mas=[]

    for row in Reader_file: # Escribir los datos de interes, coordenada temporal y radial
        list_t.append(float(row[0])/M)
        list_r.append(float(row[1])/M)
        list_r_mas.append(r_mas/M)

    csv_file.close()

    plt.plot(list_t,list_r) # Crear la grafica con los ejes y título indicado
    plt.plot(list_t,list_r_mas , linestyle='dashed', color='red', linewidth=2) # Graficar Horizonte de Eventos
    plt.xlabel('t/M')
    plt.ylabel('r/M')
    plt.title(graf_name)
    plt.ylim(0)

    plt.savefig('./Graphics/'+ graf_name +'.pdf', bbox_inches='tight') # Guardar la imagen como un pdf
    plt.savefig('./Graphics/'+ graf_name +'.png', bbox_inches='tight') # Guardar la imagen como un png

    plt.show()

    return None

def plot_taur(): # Funcion para la grafica (r/M, tau/M), hemos tomado c=1. 

    graf_name="tau frente a r"
    r_mas=r_Horizon()

    csv_file= open('./Data/Specific_Geodesic.csv', 'r') #Leer el fichero de los datos de la geodesica
    Reader_file = csv.reader(csv_file)

    list_tau=[]
    list_r=[] 
    list_r_mas=[]

    for row in Reader_file: # Escribir los datos de interes, tiempo propio y coordenada radial
        list_tau.append(float(row[4])/M)
        list_r.append(float(row[1])/M)
        list_r_mas.append(r_mas/M)

    csv_file.close()

    plt.plot(list_tau,list_r) # Crear la grafica con los ejes y título indicado
    plt.plot(list_tau,list_r_mas , linestyle='dashed', color='red', linewidth=2) # Graficar Horizonte de Eventos
    plt.xlabel('tau/M')
    plt.ylabel('r/M')
    plt.title(graf_name)
    plt.ylim(0)

    plt.savefig('./Graphics/'+graf_name+ '.pdf', bbox_inches='tight') # Guardar la imagen como un pdf
    plt.savefig('./Graphics/'+graf_name+ '.png', bbox_inches='tight') # Guardar la imagen como un png

    plt.show()

    return None


def Polar_plot(): #Funcion para la grafica de x,y del ultimo apartado del ejercicio 3

    r_mas=r_Horizon()

    csv_file= open('./Data/Specific_Geodesic.csv', 'r') #Leer el fichero de los datos de la geodesica
    Reader_file = csv.reader(csv_file)

    list_phi=[]
    list_r=[] 

    for row in Reader_file: # Escribir los datos de interes, coordenada azimutal y coordenada radial
        list_phi.append(float(row[2]))
        list_r.append(float(row[1]))

    csv_file.close()


    list_phi_horizon=np.linspace(0,2*math.pi,len(list_phi))
    x_hor=[]
    y_hor=[]
    for angle in list_phi_horizon:
        x_hor.append(math.cos(angle)*r_mas)
        y_hor.append(math.sin(angle)*r_mas)



    x=[] # Inicializamos un par de listas para guardar los datos que vamos a graficar
    y=[]
    for i in range(len(list_phi)): # EL menos phi_0 se pone para que el eje x siempre haga referencia al mismo eje y se vea la imagen claramente
        x.append(math.cos(list_phi[i]-phi_0_Geo)*math.sqrt(list_r[i]**2+constantes["a"]**2))
        y.append(math.sin(list_phi[i]-phi_0_Geo)*math.sqrt(list_r[i]**2+constantes["a"]**2))

    plt.plot(x,y)
    plt.plot(x_hor, y_hor , linestyle='dashed', color='red', linewidth=2) # Graficar Horizonte de Eventos
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title("xy")
    plt.axis('equal')

    plt.savefig('./Graphics/xy.pdf', bbox_inches='tight') # Guardar la imagen como un pdf
    plt.savefig('./Graphics/xy.png', bbox_inches='tight') # Guardar la imagen como un png

    plt.show()

    return None 