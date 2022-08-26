# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 22:11:47 2022

@author: gabri
"""

"""
TODO Section
Usando o dataset Pokemon.csv, resolva as seguintes questões:
1) crie uma função que receba o dataset e o atributo e retorne 
um histograma que mostre a distribuição do valor dos atributos 
“attack”, “defense”,”Sp.Atk”, “Sp.Def” e “Speed”. 
Insira uma linha indicando o valor médio do atributo.

2) crie um scatter plot comparando ataque (eixo x) e 
defesa (eixo y) de pokemons dos tipos Fire
e Water.

3) Utilizando o dataset Pokemon, crie um gráfico de barras que mostre, para cada geração, a proporção de pokemons Lendários e aqueles que não são lendários. Use stacked bar. 

"""
#1
import pandas as pd
import matplotlib.pyplot as plt
poke = pd.read_csv('pokemon.csv')


def  distribuicaoAtributo(dt,atributo):
    plt.figure(figsize=[10,10]).add_subplot(1, 1, 1).hist(dt[atributo],color='b', alpha=0.3)
    plt.axvline(dt[atributo].mean(),color='k',linestyle="dashed",linewidth=1)
#distribuicaoAtributo(poke,'Attack')
#distribuicaoAtributo(poke,'Defense')

#2
print(poke.columns)

fire = poke[["Attack","Defense"]][poke["Type 1"] =="Fire"]
water = poke[["Attack","Defense"]][poke["Type 1"] =="Water"]
print(fire)
print(water)
fig = plt.figure(figsize=[10,10]).add_subplot(1, 1, 1)
fig.scatter(fire["Attack"],fire["Defense"],color="b")
fig.scatter(water["Attack"],water["Defense"],color="r")

#3

print (poke.groupby())

