# Desenvolva um programa em Python que peça ao usuário para inserir dois números decimais e calcule a diferença absoluta entre esses dois números. Utilize a função nativa abs para garantir que o resultado seja sempre positivo e round para arredondar o resultado para duas casas decimais.


p1 = float(input('Digite um número: '))
p2 = float(input('Digite outro número: '))

gap = abs(p1 - p2)
result = round(gap,2)
print(result)

