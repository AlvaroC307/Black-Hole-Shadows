# Importar Librerias utiles

from Initial_Values import M, t_0, r_0, phi_0, theta_0, N_pix, Factor_Screen, Back_Im, constantes

print(M, t_0, r_0, phi_0, theta_0, N_pix, Factor_Screen, Back_Im, constantes)
param={'M':M, **constantes}
print(param)
print(Back_Im)
