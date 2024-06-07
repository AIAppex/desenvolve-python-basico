# Crie uma lista com 20 elementos, entre -10 e 10, gerados aleatoriamente. Em seguida encontre o intervalo que possui a maior quantidade de números negativos e delete ele da lista com o operador del. Você deve imprimir a lista antes e depois da deleção.

# Original: [9, 2, -1, 4, -2, -3, 5, 6, -7, -4, -1, 6, 8, -3, -6]
# Editada:  [9, 2, -1, 4, -2, -3, 5, 6, 6, 8, -3, -6]

import random

lista = [random.randint(-10, 10) for _ in range(20)]
print("Lista original:", lista)

max_neg_count = 0
start_index = 0
end_index = 0
for i in range(len(lista)):
    neg_count = 0
    for j in range(i, len(lista)):
        if lista[j] < 0:
            neg_count += 1
        if neg_count > max_neg_count:
            max_neg_count = neg_count
            start_index = i
            end_index = j

del lista[start_index:end_index+1]
print("Lista editada:", lista)
