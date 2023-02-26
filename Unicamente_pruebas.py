# Importar Librerias utiles

import math
from math import *
import csv
import Function_Metric
from Function_Metric import *


from turtle import Screen, Turtle

PIXEL_SIZE = 30
CURSOR_SIZE = 20

COLORS = {
    'B': 'blue',
    'K': 'black',
    'O': 'orange',
    'R': 'red',
    'T': 'brown',
    'W': 'white',
    'Y': 'yellow',
}

PIXELS = [
    "WWWRRRRRRWWWW",
    "WWRRRRRRRRRRW",
    "WWTTTOOOKOWWW",
    "WTOTOOOOKOOOW",
    "WTOTTOOOOKOOO",
    "WTTOOOOOKKKKW",
    "WWWOOOOOOOOWW",
    "WWRRBRRRRWWWW",
    "WRRRBRRBRRRWW",
    "RRRRBBBBRRRRW",
    "OORBYBBYBROOW",
    "OOOBBBBBBOOOW",
    "OOBBBBBBBBOOW",
    "WWBBBWWBBBWWW",
    "WTTTWWWWTTTWW",
    "TTTTWWWWTTTTW",
]

WIDTH, HEIGHT = len(PIXELS[0]), len(PIXELS)

screen = Screen()
screen.setup((WIDTH + 3) * PIXEL_SIZE, (HEIGHT + 3) * PIXEL_SIZE)
screen.tracer(False)

turtle = Turtle()
turtle.hideturtle()
turtle.shape('square')
turtle.shapesize(PIXEL_SIZE / CURSOR_SIZE)
turtle.penup()

x0 = -WIDTH/2 * PIXEL_SIZE
y0 = HEIGHT/2 * PIXEL_SIZE


for i, row in enumerate(PIXELS):
    print(i)
    turtle.setposition(x0, y0 - i * PIXEL_SIZE)

    for pixel in row:
        turtle.color(COLORS[pixel])
        turtle.stamp()
        turtle.forward(PIXEL_SIZE)

screen.tracer(True)
screen.exitonclick()


