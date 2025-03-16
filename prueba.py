import numpy as np
import random as rnd
import time 


time_start = time.time()

N=50000000

a=[]

for i in range (N):
    a.append(rnd.randint(0,1000))


b = np.sum(a)

print(b)
print(f"Ha tardado: {time.time()-time_start} segundos")