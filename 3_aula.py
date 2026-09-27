#3 tutorial do org numpy
#------------------------------------------------------------------------
import numpy as np 
import sympy as sp
#       |
#       |______________________> biblioteca para algebra 

#declaração algebrica
x=sp.Symbol('x')            #declarando variavel simbolica


a = np.array([[1, 2, 8],[ 14, 5, 6],[ 14, 5, 6]])

print('matriz')
print(a)
print('')

print('dimensoes')
print(a.ndim)

print('linha , coluna')
print(a.shape)

print('numero de elementos')
print(a.size)

print('diagonal principal')

 #              |-------------------------> função que extrai a diagonal principal da matriz
diagonal=np.diagonal(a)

print(diagonal)
print('')


print(a - (diagonal-x))

#matrizes complexas-------------------------------------------------------------------------------------------------------------------------

print( '' )    #-------------------------------------------------> Matriz com números complexos = j = (-1)^(1/2)   
c=np.array([[1+1j,2+3j],[2,3]],dtype=np.complex128 )
#                                  |________________________________________________identação para incluir numero comp. com double-precision   
print(c)