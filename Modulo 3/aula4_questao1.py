# 1) Escreva um programa que lê dois números e informa se a sua soma é par ou ímpar. Critério: se o resto da divisão do número por 2 for 0, o número é par, caso contrário é ímpar. Lembre-se do operador do python % que retorna o resto de uma divisão.

def verificar_soma():
    
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    
    soma = num1 + num2

    
    if soma % 2 == 0:
        print("A soma ({}) é par.".format(soma))
    else:
        print("A soma ({}) é ímpar.".format(soma))


verificar_soma()
