#Crie uma lista vazia chamada my_list.
#Anexe os seguintes elementos a my_list: 10, 20, 30, 40.
#Insira o valor 15 na segunda posição da lista.
#Estenda my_list com outra lista: [50, 60, 70].
#Remova o último elemento de my_list.
#Classifique my_list em ordem crescente.
#Localize e imprima o índice do valor 30 em my_list.

my_list = []

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

my_list.insert(1, 15)

my_list.extend([50, 60, 70])

my_list.pop()

my_list.sort()

index_30 = my_list.index(30)
print("Índice do valor 30 em my_list:", index_30)