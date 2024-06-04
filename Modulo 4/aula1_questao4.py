# Transforme em código o fluxograma a seguir

N = int(input('Digite um número: '))
maior = 0

while N > 0:
    x = int(input('Digite outro número: '))
    if x > maior:
        maior = x
    N -= 1

print('O maior número digitado é:', maior)

