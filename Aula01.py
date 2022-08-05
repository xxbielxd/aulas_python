# TODO: utilizando a mesma variável, ajuste cada número para que este contenha apenas 2 números após a casa decimal
# Dica: https://docs.python.org/3/library/functions.html#round
# Dica: para acessar um elemento de uma lista: lista[indice]
some_list = [1.2345, 2.1234, 4.9876, 5.0912, 3.5687]

# TODO: O laço a seguir percorre uma lista do número 2 até o número 15. 
# Toda vez que um número par for encontrado, faça: print ("Número par encontrado: ", num) e vá para o início do laço
# Ao encontrar o número 12, faça: print ("Número 12 encontrado"), e encerre o programa
for key,value in enumerate(some_list):
    some_list[key] = round(value,2)

print(some_list)

for i in range(2,15):
    if i == 12:
        print ("Número 12 encontrado")
        break
    if i % 2 == 0:
        print ("Número par encontrado: ", i)
        continue
 
### Exemplos interessantes:
## Interpolação 
print ('Agora são %02d:%02d.' % (8, 30))
print ('Percentagem: %.1f%%, Exponencial:%.2e' % (5.333, 0.00314)) #casa decimal e formatação
print ('Decimal: %d, Octal: %o, Hexadecimal: %x' % (10, 10, 10)) #bases numéricas

# Caracteres antecipados por \ são interpretados como caracteres especiais; 
# se você quer evitar isso, use raw strings, adicionando um r antes da primeira aspas

print ('C:\some\name')
print (r'C:\some\name')

## Dicionario

carros = {'marca':'Ford','modelo':'Mustang','Ano':1964} #cria um dicionário
print(carros['modelo']) #imprime o valor da chave 'modelo'
print(carros.get('Ano')) #imprime usando método get
carros['Ano'] = 2018

# Laço 
for x,y in carros.items():#imprimindo keys e values
    print(x,y)

#criando a partir de um construtor
carros = dict(marca=['Ford','FIAT','Wolksvagem'],modelo=['Mustang','Palio','Gol'],Ano=[1964,2009,1990])
print(carros)

#Diferença entre dict e default dict
d = {'key1':1, 'key2':2}
print(d['key1'])
#print(d['key3']) <- da erro
from collections import defaultdict

d = defaultdict(int)
d["key1"] = 1
d["key2"] = 2
 
print(d["key1"])
print(d["key2"])
print(d["key3"])

## Exercicios 

#1) Escreva um programa que vá de 0 até 100. Toda vez que encontrar um número divisível por 5, adicione esse número numa lista. Ao final, ordene a lista de forma descendente

listaNumeros = []
for n in range(0,101):
    if n % 5 == 0:
        listaNumeros.append(n)
print(sorted(listaNumeros,reverse=True))

#2) Conte a quantidade de cada caracter presente no texto abaixo:
#Texto
#Brasil, oficialmente República Federativa do Brasil é o maior país da América do Sul e da região da América Latina, sendo o quinto maior do mundo em área territorial (equivalente a 47 porcento do território sul-americano) e sexto em população (com mais de 200 milhões de habitantes). É o único país na América onde se fala majoritariamente a língua portuguesa e o maior país lusófono do planeta, além de ser uma das nações mais multiculturais e etnicamente diversas, em decorrência da forte imigração oriunda de variados locais do mundo.
texto = "Brasil, oficialmente República Federativa do Brasil é o maior país da América do Sul e da região da América Latina, sendo o quinto maior do mundo em área territorial (equivalente a 47 porcento do território sul-americano) e sexto em população (com mais de 200 milhões de habitantes). É o único país na América onde se fala majoritariamente a língua portuguesa e o maior país lusófono do planeta, além de ser uma das nações mais multiculturais e etnicamente diversas, em decorrência da forte imigração oriunda de variados locais do mundo.";
from collections import Counter
word_counts_counter = Counter(texto)
print(word_counts_counter);

#3) Solicite ao usuário uma string e um número inteiro. Armazene ambos em variáveis. Remova da string os caracteres de 0 até n e imprima a string resultante
inputString = input("Escreva uma string: ")
inputNum = int(input("Agora escreva um número: "))

print(inputString[inputNum:])

