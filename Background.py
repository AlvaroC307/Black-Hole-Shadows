import math
import os
from PIL import Image

def Sphere_Quadrants(r, phi, theta):
    # Cambio de coordenadas esfericas a cartesianas (la coordenada y no afecta en nada, ya que z es la altura, x es izqa o derecha)
    # Se usa esfericas en vez de oblatas porque esto se evalua en r->10M, por lo que son aproximadamente esfericas
    x=r*math.cos(phi)*math.sin(theta) #el sin(theta) no sirve de nada aqui¿?¿?¿?¿?
    z=r*math.cos(theta)

    # Los cuadrantes son: 1) Green, 2) Red, 3) Yellow, 4) Blue
    if (z>0) and (x>0):
        return "Green"  # Primer cuadrante para z>0, x>0
    elif (z>0) and (x<0):
        return "Red"   # Segundo cuadrante para z>0, x<0
    elif (z<0) and (x<0):
        return "Yellow" # Tercer cuadrante para z<0, x<0
    elif (z<0) and (x>0):
        return "Blue"   # Cuarto cuadrante para z<0, x>0
    else:
        return "White" # z=0 or x=0
    

def Background_Image(r, phi, theta, r_limit):


    N_pix=28

    N_I=N_pix

    # Cambio de coordenadas esfericas a cartesianas (la coordenada y no afecta en nada, ya que z es la altura, x es izqa o derecha)
    # Se usa esfericas en vez de oblatas porque esto se evalua en r->10M, por lo que son aproximadamente esfericas
    x=r*math.cos(phi)*math.sin(theta)
    z=r*math.cos(theta)

    eps=1 # Esto quizá pueda cambiar al cambiar r_limit, mirar la función de paso adaptativo
    L_I=2*r_limit #+ eps  
    paso_x = N_pix / L_I
    paso_z = N_pix / L_I

    Pix_x=(N_I/2)+int(paso_x*x)
    Pix_z=(N_I/2)+int(paso_z*z)



    # Abrir la imagen y conseguir sus dimensiones
    current_dir = os.getcwd()
    file_path = current_dir + '/Graphics/Background_Prueba.png'

    image=Image.open(file_path)
    width, height = image.size

    pixel_width = width // N_I
    pixel_height = height // N_I


    # Get the pixel color 
    pixel_color = image.getpixel((Pix_x, Pix_z))
    Color= list(pixel_color) # Camiar una tupla  a una lista de tres elementos RGB    

    return Color



Background_Image(10, math.pi/2, math.pi/2, 10)

