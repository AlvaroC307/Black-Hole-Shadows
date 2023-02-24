import math



def Sphere_Quadrants(r, phi, theta):
    # Cambio de coordenadas esfericas a cartesianas (la coordenada y no afecta en nada, ya que z es la altura, x es izqa o derecha)
    x=r*math.cos(phi)*math.sin(theta)
    z=r*math.cos(theta)

    # Los cuadrantes son: 1) Green, 2) Red, 3) Yellow, 4) Blue
    if (z>0) and (x>0):
        return "Green"
    elif (z>0) and (x<0):
        return "Red"
    elif (z<0) and (x<0):
        return "Yellow"
    elif (z<0) and (x>0):
        return "Blue"
    else:
        return "None"