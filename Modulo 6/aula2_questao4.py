# Crie um programa em Python que receba duas listas de números do usuário, podendo cada lista ter uma quantidade diferente de valores. Em seguida, combine essas duas listas de forma alternada para formar uma terceira lista. Intercale os elementos até o final da primeira lista, adicionando ao final os elementos remanescentes da maior lista.
# Exemplo de interação via terminal (entradas em negrito):
# Digite a quantidade de elementos da lista 1: 4
# Digite os 4 elementos da lista 1:
# 1
# 2
# 3
# 4Digite a quantidade de elementos da lista 2: 6
# Digite os 6 elementos da lista 2:
# 5
# 6
# 7
# 8
# 9
# 10Lista intercalada: 1 5 2 6 3 7 4 8 9 10

def intercalar_listas(lista1, lista2):
    resultado = []

    tamanho_menor = min(len(lista1), len(lista2))

    for i in range(tamanho_menor):
        resultado.append(lista1[i])
        resultado.append(lista2[i])

    resultado.extend(lista1[tamanho_menor:])
    resultado.extend(lista2[tamanho_menor:])

    return resultado


quantidade_lista1 = int(input('Digite a quantidade de elementos da lista 1: '))
lista1 = [int(input(f'Digite o {i+1}º elemento da lista 1: ')) for i in range(quantidade_lista1)]
quantidade_lista2 = int(input('Digite a quantidade de elementos da lista 2: '))
lista2 = [int(input(f'Digite o {i+1}º elemento da lista 2: ')) for i in range(quantidade_lista2)]


lista_intercalada = intercalar_listas(lista1, lista2)

print('Lista intercalada:', *lista_intercalada)
