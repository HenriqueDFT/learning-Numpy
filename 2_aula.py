#2 tutorial do org numpy
#------------------------------------------------------------------------
import numpy as np 


a = np.array([1, 2, 8, 4, 5, 6])
a = a[3:]  # estou contando a partir do terceiro elemento para frente
print(a)
print('')


a = np.array([[1, 2, 8],[4, 5, 6]])
a = a[:,1:]  
               # estou contando a partir do segundo elemento da primeira linha e a segunda linha 
               ## Seleciona TODAS as linhas (:)


b = np.array([(1,2)])
b.shape=(1,2) 
b[:,:] = 40  # Altera todos os elementos de b para 40

print(a)   # 'a' também mudou! Resultado: [10, 2, 3, 40, 5, 6]
print(b)

#-------------------------------------------------------------------------

#3 tutorial do org numpy
#------------------------------------------------------------------------
import numpy as np 


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

print('teste de mudar o tipo')

