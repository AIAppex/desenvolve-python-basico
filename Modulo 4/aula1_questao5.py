# Um instituto realizou uma pesquisa de público e precisa calcular a média de idade dos respondentes. Escreva um programa que leia um inteiro N com a quantidade de respondentes e em seguida leia as N idades de cada respondente. Ao final, imprima a média das idades.

N = int(input("Digite a quantidade de respondentes: "))
soma_idades = 0

for _ in range(N):
    idade = int(input("Digite a idade do respondente: "))
    soma_idades += idade

media_idades = soma_idades / N
print('A média das idades é: {}'.format(media_idades))
