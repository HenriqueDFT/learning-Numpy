#1 tutorial do org numpy
#------------------------------------------------------------------------
import numpy as np 

a=np.array([[1,0],[2,3]]) #declaração da matriz [[linha 1][linha2]] termos dado na ordem 0,1,2,3,4,5,6,7... ou seja, partimos a contagem do 0
a.shape=(2,2)

print(a)
print(a[1,0])

#atualizando a matriz
a[0,0]=10
# | |_________________________>elemento da matriz
# |___________>linha
# caso coloque apenas a linha : a[0]= 10, significa que todo elemento da linha 1, será igual a 10.


print(a+1)#soma de matrizes é operada corretamente

#teste de multiplicação, testamos pela identidade

#matriz identidade I
print('')
I=np.identity(2)
print(I)
print('')

print('produto de matrizes')
print('')

print(a ,'*',I)
print('')
print(a*I)
#com isso verificamos que o produto matricial não é feito de forma direta, precisamos chamar o produto
