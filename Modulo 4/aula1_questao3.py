# Transforme em código o fluxograma a seguir

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))

m = (n1+ n2+ n3)/3

while True:
    if m >= 60:
        print('Aprovado')
        break
    elif m >= 40:
        print('Recuperação')
        break
    else:
        print('Reprovado')
        break
print('Fim')

