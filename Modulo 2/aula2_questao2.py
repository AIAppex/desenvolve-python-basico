# 2) Transforme o seguinte algoritmo em código. Lembre-se das funções print e type que já conhecemos de forma geral.
# Armazene o texto "o resultado é"  em uma variável, o valor 10 em outra variável, e o valor 3.5 numa terceira variável.
# Some os valores da segunda e terceira variável e armazene em outra variável.
# Imprima todas as variáveis na ordem de criação e imprima também seus tipos.

texto = 'O resultado é'
valor1 = 10
valor2 = 3.5

resu = valor1 + valor2

print('{}: {} + {} = {}'.format(texto, valor1, valor2, resu))
print('Tipo de texto:', type(texto))
print('Tipo de valor 1:', type(valor1))
print('Tipo de valor 2:', type(valor2))
print('Tipo de resultado:', type(resu))