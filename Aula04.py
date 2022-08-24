# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 21:47:22 2022

@author: gabri
"""

import numpy as np


"""
1)
Seja um array, A = [10,3,7,5,8,23,15] e dois escalares, x = 6, y = 20.

Crie uma função que retorne um novo array contendo elementos no intervalo [6,20]
"""

A = [10,3,7,5,8,23,15]
a = np.array(A)


def filtrar(array,x,y):
   
    return array[np.logical_and(array>x,array<y )]

resultado = filtrar(a,6,20)

print(resultado)

"""

2)
Escreva um programa usando Numpy que adiciona os valores de um vetor a cada linha de uma matriz.

Obs: o tamanho do vetor tem de ser o mesmo da quantidade de linhas

vetor = [ 1 1 0]

matriz = [1 2 3; 4 5 6; 7 8 9]

resultado = [2 3 3; 5 6 6; 8 9 9]

Essa função pode ajudar: np.empty_like()

"""


matriz = [[1,2,3],[4,5,6],[7,8,9]]
m = np.array(matriz)

print(matriz + np.array([1,1,0]))

"""
3)
Suponha dois arrays, A = [1,4,2,6,5,7,3,0] e B = [3,2,0,9,8,7].

Remove de A todo elemento pertencente a B
"""


A = np.array([1,4,2,6,5,7,3,0])
B = np.array([3,2,0,9,8,7])

AB = np.setdiff1d(A,B)
print (AB)

"""
4)
A célula abaixo faz o download de um dataset e armazena na variável iris_2d. Em seguida, substitui alguns de seus elementos por NaN. Resolva as questões que se seguem:
"""

import numpy as np
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])
iris_2d[np.random.randint(150, size=20), np.random.randint(4, size=20)] = np.nan

"""
a) Encontre o número de NaN na primeira coluna

b) Encontre o número total de NaN

c) Encontre as posições (número da linha) de NaN na primeira coluna

d) Substitua todos os NaN por 0
"""
coluna1 = iris_2d[:,0]
emBranco = np.isnan(coluna1)

#ESTA INCOMPLETO 




