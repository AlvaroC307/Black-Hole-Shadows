import Background as bg
import csv
from Initial_Values import N_pix

# Leer la x y la y del fichero de colores
# Abrir el fichero con los colores a lee
file_Total_Color = open('./Data/Geodesics_Color.csv', 'r')
Reader_Total_Color = csv.reader(file_Total_Color)

ijxy_Total=[] # Lista de Listas donde estarán todos los colores como string
k=0
for row in Reader_Total_Color:
    ijxy=[row[0], row[1], row[3], row[4]] # El color está en la tercera columna, el resto indican en que lugar está
    ijxy_Total.append(ijxy)


#print(ijxy_Total[23][1])
file_Total_Color.close()


file_Position = open("./Data/Geodesics_Position_Total.csv", 'r')
csv_Position = csv.reader(file_Position)
file_Color = open("./Data/Geodesics_Color.csv", "w", newline="")
csv_Color = csv.writer(file_Color)


progreso=100/(N_pix**2)
k=0
for row in csv_Position:
    if (row[0]=="Inside"):
        Pixel_Color="Black"
    elif (row[0]=="Orbit"):
        Pixel_Color="Pink"
    else: 
        Pixel_Color=bg.Background_Image(eval(row[0]), eval(row[1]), eval(row[2]))

    csv_Color.writerow([ijxy_Total[k][0], ijxy_Total[k][1], Pixel_Color, ijxy_Total[k][2], ijxy_Total[k][3]])
    k+=1
    print(k*progreso)

