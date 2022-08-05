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
 