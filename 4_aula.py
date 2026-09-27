#tutorial_4
import numpy as np
import math as mt
import sympy as sp

a=np.zeros((3, 3)) #matriz 3x3 em zeros
b=np.diagonal(a+1)
print(a)
print(b)

print('----------------------------------------------------')
b=np.ones((2, 3, 4,5), dtype=np.int16) #matriz 4x5 ~ ou seja, numpy so interpreta os dois ultimos
print(b)
c=np.empty((2, 3))# matrizes com valores pequenos
print(c)


#  |----------------->lista numerica
#  |        |-------->inicio da lista
#  |        |    |------------------------------------------>passos
v=np.arange(3,5,0.1)                                                       #aceita floats e int
#             |__________>limite, no caso não é atingido 

print(v)



