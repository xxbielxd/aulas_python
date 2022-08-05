some_list = [1.2345, 2.1234, 4.9876, 5.0912, 3.5687]

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
 