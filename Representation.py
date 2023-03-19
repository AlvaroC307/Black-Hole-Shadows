# Leer los ficheros de resultados para representarlo en un dibujo
import csv
import math
from turtle import Screen, Turtle, getcanvas
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

def tortuga():

    file_Total = open('./Data/Geodesics_Total.csv', 'r')
    Reader_Total = csv.reader(file_Total)

    List_Total=[]

    for row in Reader_Total:
        content=[int(row[0]), int(row[1]), row[2]]
        List_Total.append(content)


    # Usando el modulo turtle para hacer un pixelart
    Pixel_Size = 10
    Cursor_Size = 20
    Draw_Size= int(math.sqrt(len(List_Total)))

    screen = Screen()
    screen.setup((Draw_Size + 3) * Pixel_Size, (Draw_Size + 3) * Pixel_Size)
    screen.tracer(False)

    turtle = Turtle()
    turtle.hideturtle()
    turtle.shape('square')
    turtle.shapesize(Pixel_Size / Cursor_Size)
    turtle.penup()

    x0 = -Draw_Size/2 * Pixel_Size
    y0 = Draw_Size/2 * Pixel_Size
    num=0

    for i in range(Draw_Size):
        turtle.setposition(x0 , y0 - i * Pixel_Size  ) #comprobar que este yendo en el sentido bueno 
        for j in range(Draw_Size):

            turtle.color(List_Total[num][2])
            turtle.stamp()
            turtle.forward(Pixel_Size)
            num=num+1

    canvas=getcanvas()
    canvas.postscript(file="./Graphics/" + "Black_Hole_Image.eps")

    screen.tracer(True)
    screen.exitonclick()



def matplot(N_pix):

    file_Total = open('./Data/Geodesics_Total.csv', 'r')
    Reader_Total = csv.reader(file_Total)

    Color_Total=[]
    Color_Line=[]
    k=0
    for row in Reader_Total:
        content=row[2]
        Color_Line.append(content)
        k+=1
        if k==N_pix:
            Color_Total.append(Color_Line)
            k=0
            Color_Line=[]


    color_array = np.array([[mcolors.to_rgba(color) for color in row] for row in Color_Total])

    # Create a figure and plot the image
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.imshow(color_array)

    # Hide the axes and show the plot
    ax.axis('off')
    plt.savefig('./Graphics/Black_Hole_Image.pdf', bbox_inches='tight')
    plt.savefig('./Graphics/Black_Hole_Image.png', bbox_inches='tight')
    plt.show()




def main():
    csv_Input = open('./Input/Input.csv', 'r')
    Reader_Input = csv.reader(csv_Input)

    list_Input = []
    for row in Reader_Input:
        content_input = row[1]
        list_Input.append(content_input)

    csv_Input.close()

    # Numero de Pixeles en un lado, el numero de pixeles total será, N_pix * N_pix
    N_pix = eval(list_Input[5])
    if (N_pix % 2) == 1:  # Para que N_pix sea par y se pueda divir facil en 4 cuadrantes
        N_pix += 1

    matplot(N_pix)

if __name__ == '__main__':
    main()
