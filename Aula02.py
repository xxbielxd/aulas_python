#TODO: Crie uma função que retorne na forma de um dicionário as seguintes 
#   informações do texto abaixo: número de palavras, número de números e número de frases.
#Dica: a função isdigit() pode ser útil para determinar o 
#   tipo de caracter; Dica: split() usa um caracter (a ser inserido dentro dos parenteses) 
#   para separar uma string
import re
def analiseFrase ( frase ) :
    totalLetras = 0
    totalNumeros = 0
    totalFrases = 0
    totalPalavras = 0
    for k,i in enumerate(frase):
        if(i.isdigit() and i.strip() ) :
            totalNumeros+=1
        elif (not i.isdigit() and i.strip()):
            totalLetras+=1
        if ((i== "," or i== ".") and (len(frase)-1 == k or frase[k+1] == " ")):
            totalFrases+=1
    palavras = frase.split(" ")
    
    for palavra in palavras :
        if(palavra.strip() and not palavra[0].isdigit()) :
            totalPalavras += 1
    
    frases = re.findall(r'.,|.\.', frase)
    print(frases)
    totalFrases = len(frases)    
    return {
        "letras": totalLetras,
        "numeros": totalNumeros,
        "palavras": totalPalavras,
        "frases": totalFrases
    }

    
retorno = analiseFrase("Brasil, oficialmente República Federativa do Brasil é o maior país da América do Sul e da região da América Latina, sendo o quinto maior do mundo em área territorial (equivalente a 47 porcento do território sul-americano) e sexto em população (com mais de 200 milhões de habitantes). É o único país na América onde se fala majoritariamente a língua portuguesa e o maior país lusófono do planeta, além de ser uma das nações mais multiculturais e etnicamente diversas, em decorrência da forte imigração oriunda de variados locais do mundo.")

print("Total de Letras: ",retorno['letras'])
print("Total de Numeros: ",retorno['numeros'])
print("Total de Palavras: ",retorno['palavras'])
print("Total de Frases: ",retorno['frases'])

#Crie uma função que receba uma data no formato yyyy-mm-dd e, usando Regex,retorne essa data no formato dd-mm-yyyy

def converterdata(data):
    
    dataList = re.findall(r".{4}-|.{2}-|.{2}",data)
    
    return dataList[2].replace("-","") + "-" +  dataList[1].replace("-","") + "-" +  dataList[0].replace("-","")
    
    
dataConvertida = converterdata("2022-01-30")

print(dataConvertida)

#Escreva uma função que receba duas datas (formato datetime '%Y-%m-%d %H:%M:%S') 
#e retorne a diferença entre elas em dias, horas, minutos e segundos

#Dica: a função divmod() pode ser útil: link

import time
import datetime
from math import ceil

def verificardifdata (data1,data2) :
    
    data1 = time.mktime(datetime.datetime.strptime(data1, "%Y-%m-%d %H:%M:%S").timetuple())
    data2 = time.mktime(datetime.datetime.strptime(data2, "%Y-%m-%d %H:%M:%S").timetuple())
    
    diferenca = data1 - data2

    minutosTotal = ceil(diferenca/60)
    segundos=diferenca%60
    
    horasTotal = ceil(minutosTotal/60)
    minutos = minutosTotal%60
    
    dias = ceil(horasTotal/24)
    horas = horasTotal%24
    
    

    return str(dias)+ "dias, " + str(horas) + " horas, " + str(minutos) + " minutos, " + str(segundos) + " segundos"


resultado = verificardifdata("2022-08-04 1:20:00", "2022-08-01 1:30:00")

print (resultado)




