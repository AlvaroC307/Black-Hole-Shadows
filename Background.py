import math

def Sphere_Quadrants(r, phi, theta):
    # Cambio de coordenadas esfericas a cartesianas (la coordenada y no afecta en nada, ya que z es la altura, x es izqa o derecha)
    # Se usa esfericas en vez de oblatas porque esto se evalua en r->10M, por lo que son aproximadamente esfericas
    x=r*math.cos(phi)*math.sin(theta)
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