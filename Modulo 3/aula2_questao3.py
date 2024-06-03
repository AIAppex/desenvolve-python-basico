# 3) Você está desenvolvendo um sistema de admissão para um clube juvenil de jogos de tabuleiro. Escreva um programa em Python que pergunte ao usuário sua idade, se já jogou pelo menos 3 jogos de tabuleiro (resposta deve ser True ou False) e quantas vezes venceu um jogo. O programa deve imprimir True, permitindo o ingresso do participante no clube, se:
# tiver entre 16 e 18 anos
# já tiver jogado pelo menos 3 jogos
# já ter vencido pelo menos 1 jogo, 
# Sua expressão deve imprimir False caso contrário. Aqui está um exemplo de interação com seu código no terminal, com entradas de dados destacadas em negrito e as impressões de seu código em itálico (apenas para facilitar sua visualização).

# Digite sua idade: 17
# Já jogou pelo menos 3 jogos de tabuleiro? True
# Quantos jogos já venceu? 2
# Apto para ingressar no clube de jogos de tabuleiro: True



    
idade = int(input("Digite sua idade: "))
jogou_tres = input("Já jogou pelo menos 3 jogos de tabuleiro?: ").lower() == "true"
venceu_jogo = int(input("Quantos jogos já venceu? "))
apto_para_ingresso = 16 <= idade <= 18 and jogou_tres and venceu_jogo >= 1

print("Apto para ingressar no clube de jogos de tabuleiro: {}".format(apto_para_ingresso))

