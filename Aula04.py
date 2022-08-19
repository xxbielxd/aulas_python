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






