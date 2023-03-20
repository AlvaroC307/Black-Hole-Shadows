# Importar Librerias utiles

import time
import csv
from math import *
from Function_Metric import *
from playsound import playsound
from concurrent.futures import *

def esperar(name):
    time.sleep(2)

    csv_file=open("./Data/Borrar.csv", "r")
    csv_reader=csv.reader(csv_file)
    content=[]
    for row in csv_reader:
        content.append(row[0])
    csv_file.close()

    return 1

def main():

    executor = ProcessPoolExecutor(max_workers=2)

    work_a=executor.submit(esperar, "a")
    work_b=executor.submit(esperar, "b")

    print(work_a.result()+work_b.result())
    playsound("./Sounds/Barra_Metal_Cayendo.mp3")
    


if __name__ == '__main__': #Llamar al main()
    main()
    


