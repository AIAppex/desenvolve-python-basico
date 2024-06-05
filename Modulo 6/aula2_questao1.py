# Faça um programa que gere aleatoriamente 20 valores inteiros entre -100 e 100 e os armazene em uma lista. Em seguida imprima na ordem estabelecida:
# A lista ordenada, sem modificar a lista original
# A lista original
# O índice do maior valor da lista
# O índice do menor valor da lista

import random

valores = [random.randint(-100, 100) for _ in range(20)]
print('Lista original:', valores)


lista_ordenada = valores.copy()
lista_ordenada.sort()
print('Lista ordenada:', lista_ordenada)

indice_maior = valores.index(max(valores))
print('Índice do maior valor: {}'.format(indice_maior))

indice_menor = valores.index(min(valores))
print('Índice do menor valor: {}'.format(indice_menor))
