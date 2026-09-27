#tutorial_4
import numpy as np
import math as mt
import sympy as sp
from numpy import pi #---------------------> extraindo pi de forma nativa ao numpy


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

#------------------visualização------------------------------------------------------------
print(v)

print('----------------exportando dat----------------------')



#      |-------------------------------------------->função de contagem com maior precisão e espaçada conforme o intervalo, calculo equidistante X_0 -X /passos
#      |        _________>X_0 
#      |        |    ------>X
#   ___|________|    |        |----->passos  
x = np.linspace(0, 2 * pi, 100)

# criando a função seno pelo numpy
f = np.sin(x)

#criando o objeto do arquivo com uma coluna (x,y)
dados = np.column_stack((x, f))
#       ---------------     
#             |
#         empilhando os valores de x e f com colunas espaçadas


# 4. Exportando para arquivo .dat
nome_arquivo = 'seno_dados.dat'

np.savetxt(                                    #criando o arquivo, np é a função que cria txt
    nome_arquivo,
    dados,
    fmt='%.4e',                  # Formato: notação científica com 4 casas decimais, ou seja, o valor indica a casa decimal
    header='x_rad f(x)',          # Cabeçalho na primeira linha
    comments='# '                 # Caractere de comentário para o cabeçalho
)

print(f"Dados exportados com sucesso para '{nome_arquivo}'.")



