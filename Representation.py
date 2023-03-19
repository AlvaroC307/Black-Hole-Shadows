# Leer los ficheros de resultados para representarlo en un dibujo
import csv
import matplotlib.pyplot as plt # Esto es para el plot
import matplotlib.colors as mcolors # Esto es para cambiar los colores a valores numéricos
import numpy as np # Esto es para los array al cambiar de los colores a valores numericos

"""from turtle import Screen, Turtle, getcanvas

    def tortuga(): # Esta funcion utiliza el modulo tortuga pero tiene problemas asi que la quitaré

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
    screen.exitonclick() """



def matplot(N_pix):
    # Abrir el fichero con los colores a lee
    file_Total = open('./Data/Geodesics_Total.csv', 'r')
    Reader_Total = csv.reader(file_Total)

    Color_Line=[] # Lista donde se apuntan los colores de una linea en el eje x entera antes de pasarla a Color_Total
    Color_Total=[] # Lista de Listas donde estarán todos los colores como string
    k=0
    for row in Reader_Total:
        content=row[2] # El color está en la tercera columna, el resto indican en que lugar está
        Color_Line.append(content)
        k+=1
        if k==N_pix:
            Color_Total.append(Color_Line)
            k=0
            Color_Line=[]

    # Cambio de la lista de listas de colores en string a un array de colores como números para matplotlib
    color_array = np.array([[mcolors.to_rgba(color) for color in row] for row in Color_Total])

    # Create a figure and plot the image
    fig, ax = plt.subplots(figsize=(5, 5)) # figsize habla sobre el tamaño de la imagen
    ax.imshow(color_array)

    # Quitar los ejes, guardar y mostrar en pantalla la imagen 
    ax.axis('off')
    plt.savefig('./Graphics/Black_Hole_Image.pdf', bbox_inches='tight') # Guardar la imagen como un pdf
    plt.savefig('./Graphics/Black_Hole_Image.png', bbox_inches='tight') # Guardar la imagen como un png
    plt.show() # Mostrar la imagen




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
