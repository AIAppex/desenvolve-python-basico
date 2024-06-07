# Escreva um script em Python que solicita do usuário uma quantidade indefinida de números inteiros (pelo menos 4 valores), os armazena em uma lista e, usando fatiamento de listas, imprima:
# A lista original
# Os 3 primeiros elementos
# Os 2 últimos elementos
# A lista invertida (do fim para o começo)
# Os elementos de índice par (0, 2, 4 … )
# Os elementos de índice ímpar (1, 3, 5, … )


numeros = []

while True:
    try:
        numero = int(input('Digite um número inteiro (ou "sair" para terminar): '))
        numeros.append(numero)
    except ValueError:
        if len(numeros) >= 4:
            break
        else:
            print('Por favor, insira pelo menos 4 valores.')

print('Lista original:', numeros)
print('Os 3 primeiros elementos:', numeros[:3])
print('Os 2 últimos elementos:', numeros[-2:])
print('Lista invertida:', numeros[::-1])
print('Elementos de índice par:', numeros[::2])
print('Elementos de índice ímpar:', numeros[1::2])
