# Leer los ficheros de resultados para representarlo en un dibujo
import csv
import math
from turtle import Screen, Turtle


file_Total = open('./Data/Geodesics_Total.csv', 'r')
Reader_Total = csv.reader(file_Total)

List_Total=[]

for row in Reader_Total:
    content=[int(row[0]),int(row[1]),row[2]]
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
turtle.right(90)

for i in range(Draw_Size):
    turtle.setposition(x0+ i * Pixel_Size , y0 ) #comprobar que este yendo en el sentido bueno 
    for j in range(Draw_Size):

        turtle.color(List_Total[num][2])
        turtle.stamp()
        turtle.forward(Pixel_Size)
        num=num+1


screen.tracer(True)
screen.exitonclick()
