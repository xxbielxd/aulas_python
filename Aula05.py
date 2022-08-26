# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 21:24:39 2022

@author: gabri
"""

"""
TODO Section
Manipulação de DataFrame
    > Crie, a partir do dicionário abaixo, um DataFrame cujo index seja os valores da variável labels
    > encontre a média dos valores da coluna age e preencha os valores faltantes dessa coluna com o valor da média
    > crie uma nova coluna chamada 'rank', que mostre os animais que receberam mais visitas
    > qual o animal que recebeu a maior quantidade de visitas?
"""
import numpy as np
import pandas as pd

data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

dataFrame = pd.DataFrame(data,index=labels)

print(dataFrame)

media = dataFrame["age"].mean()
dataFrame.fillna(0)
dataFrame = dataFrame.fillna(media)
dataFrame['rank'] = dataFrame['visits'].rank(ascending=1)
print(dataFrame)

maior = dataFrame["rank"].argmax()

print(dataFrame.iloc[maior])

print(maior)

print (media)



"""

TODO Section
Manipulação de Dados usando Pandas
Usando o dataset Pokemon.csv, faça:

1) Verifique em qual(is) coluna(s) existem valores faltantes
2) Preencha os valores faltantes da coluna Type 2 com os valores correspondentes da coluna Type 1
3) Crie um DataFrame a partir dos dados originais contendo apenas pokemons lendários. Imprima os 5 primeiros
4) Use apply/applymap para passar todos os valores das colunas Name, Type 1 e Type 2 para minúscula
5) Agrupe os pokemons por Type 1 e retorne uma Série ordenada pela quantidade em ordem decrescente
"""

# 1
import pandas as pd
poke = pd.read_csv('pokemon.csv')
notnullpoke = poke.dropna(axis=1).columns
nullpoke =   set(poke.columns.tolist()) - set(notnullpoke.tolist())
print (nullpoke)


# 2
poke['Type 2'].fillna(poke['Type 1'], inplace = True)

# 3

print(poke.columns)

lendarios = poke[poke["Legendary"]== True]

print(lendarios)

#4

poke["Name"] = poke["Name"].map(lambda x:x.upper())
poke["Type 1"] = poke["Type 1"].map(lambda x:x.upper())
poke["Type 2"] = poke["Type 2"].map(lambda x:x.upper())

print(poke)
group1 = poke["Type 1"]
group = poke.groupby("Type 1").size()

print (group)



