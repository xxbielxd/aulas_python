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
import numpy as np
poke = pd.read_csv(r'C:\git\aulas_python\pokemon.csv')


def  distribuicaoAtributo(dt,atributo):
    plt.figure(figsize=[10,10]).add_subplot(1, 1, 1).hist(dt[atributo],color='b', alpha=0.3)
    plt.axvline(dt[atributo].mean(),color='k',linestyle="dashed",linewidth=1)
#distribuicaoAtributo(poke,'Attack')
#distribuicaoAtributo(poke,'Defense')

#2
print(poke.columns)

fire = poke[["Attack","Defense"]][poke["Type 1"] =="Fire"]
water = poke[["Attack","Defense"]][poke["Type 1"] =="Water"]

#fig = plt.figure(figsize=[10,10]).add_subplot(1, 1, 1)
#fig.scatter(fire["Attack"],fire["Defense"],color="b")
#fig.scatter(water["Attack"],water["Defense"],color="r")

#3
N = 6
group = poke.groupby(['Generation','Legendary']).size().reset_index(name='count')
lendarios = group[group['Legendary']==True].reset_index()
naolendarios = group[group['Legendary']==False].reset_index()


ind = np.arange(N)    
width = 0.35       # largura das barras

p1 = plt.bar(naolendarios["Generation"], naolendarios["count"], width)
p2 = plt.bar(lendarios["Generation"], lendarios["count"], width,
             )
plt.ylabel('Quantidade de Lendarios')
plt.title('Quantidade de pokemons por geração')
plt.xticks(naolendarios["Generation"])
plt.yticks(lendarios["count"]+naolendarios["count"])
plt.legend((p1[0], p2[0]), ( 'Não lendários','Lendários',))
for x,y,val in zip(lendarios["Generation"],lendarios["count"]/2, lendarios["count"]):
    plt.text(x, y, "%.1d"%val, ha="center", va="center")
for x,y,val in zip(lendarios["Generation"],lendarios["count"]+naolendarios["count"]/2, naolendarios["count"]):
    plt.text(x, y, "%.1d"%val, ha="center", va="center")

plt.show()




