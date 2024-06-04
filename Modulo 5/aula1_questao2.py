# Escreva um código que gere n valores inteiros aleatórios entre 0 e 100 e calcule a raíz quadrada da soma dos valores. Peça ao usuário o valor de n

import random
import math

soma = 0 

p1 = int(input('Digite o valor de p1: '))
for i in range(1, p1 + 1):
    numero_aleatorio = random.randint(1, 100)
    print('Número aleatório gerado: {}'.format(numero_aleatorio))
    soma += numero_aleatorio

resultado = math.sqrt(soma)

print('Raiz quadrada da soma: {}'.format(resultado))
