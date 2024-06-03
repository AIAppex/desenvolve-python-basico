# 4) Escreva um programa que leia um valor inteiro referente a uma quantia em reais e calcule a menor quantidade possível de notas necessárias para pagar aquele valor. As notas possíveis são: 100, 50, 20, 10, 5, 2, 1. A saída deve estar formatada exatamente como indicado. 

# Entrada:
# 576

# Saída:
# 5 nota(s) de R$100,00
# 1 nota(s) de R$50,00
# 1 nota(s) de R$20,00
# 0 nota(s) de R$10,00
# 1 nota(s) de R$5,00
# 0 nota(s) de R$2,00
# 1 nota(s) de R$1,00

# Solicita o valor em reais
valor_reais = int(input("Digite o valor em reais: "))

# Contador de notas
notas_100 = 0
notas_50 = 0
notas_20 = 0
notas_10 = 0
notas_5 = 0
notas_2 = 0
notas_1 = 0

while valor_reais > 0:
    if valor_reais >= 100:
        notas_100 += 1
        valor_reais -= 100
    elif valor_reais >= 50:
        notas_50 += 1
        valor_reais -= 50
    elif valor_reais >= 20:
        notas_20 += 1
        valor_reais -= 20
    elif valor_reais >= 10:
        notas_10 += 1
        valor_reais -= 10
    elif valor_reais >= 5:
        notas_5 += 1
        valor_reais -= 5
    elif valor_reais >= 2:
        notas_2 += 1
        valor_reais -= 2
    else:
        notas_1 += 1
        valor_reais -= 1



print("{} nota(s) de R$100,00".format(notas_100))
print("{} nota(s) de R$50,00".format(notas_50))
print("{} nota(s) de R$20,00".format(notas_20))
print("{} nota(s) de R$10,00".format(notas_10))
print("{} nota(s) de R$5,00".format(notas_5))
print("{} nota(s) de R$2,00".format(notas_2))
print("{} nota(s) de R$1,00".format(notas_1))
