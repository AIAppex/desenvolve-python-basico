# 2) Leia um valor inteiro correspondente a uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius.
# Fórmula de conversão: C = (F - 32) * (5/9), sendo C o valor em graus Celsius e F o valor em Fahrenheit. Antes de imprimir, converta o valor em Celsius para inteiro. A mensagem deve estar formatada da seguinte maneira:

# 86 graus Fahrenheit são 30 graus Celsius.

# Solicita uma temperatura em Fahrenheit
fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))

# Calcula a temperatura em Celsius
celsius = int((fahrenheit - 32) * (5/9))

print("{} graus Fahrenheit são {} graus Celsius.".format(fahrenheit, celsius))
