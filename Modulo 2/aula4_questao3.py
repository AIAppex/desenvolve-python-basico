# 3) Você está desenvolvendo um programa para calcular o preço total de uma compra em uma loja online. O preço dos produtos é calculado multiplicando a quantidade pelo preço unitário. Escreva um programa em Python que solicite do usuário o nome, o preço unitário e a quantidade de 3 produtos comprados e imprima ao final o preço total da compra. Note no exemplo a seguir que:
# Cada entrada de dados tem uma mensagem indicando o dado solicitado (mensagens em itálico, dado de entrada em negrito).
# A saída deve estar formatada exatamente como indicado (a string "Total: R$" e o preço com um separador de milhar e duas casas decimais).
# Entrada:
# Digite o nome do produto 1: calça
# Digite o preço unitário do produto 1: 199.90
# Digite a quantidade do produto 1: 3
# Digite o nome do produto 2: camisa
# Digite o preço unitário do produto 2: 49.95
# Digite a quantidade do produto 2: 10
# Digite o nome do produto 3: cinto
# Digite o preço unitário do produto 3: 25
# Digite a quantidade do produto 3: 3

# Saída:
# Total: R$1,174.20

# Solicita os dados dos produtos
nome_produto1 = input("Digite o nome do produto 1: ")
preco_unitario1 = float(input("Digite o preço unitário do produto 1: "))
quantidade1 = int(input("Digite a quantidade do produto 1: "))

nome_produto2 = input("Digite o nome do produto 2: ")
preco_unitario2 = float(input("Digite o preço unitário do produto 2: "))
quantidade2 = int(input("Digite a quantidade do produto 2: "))

nome_produto3 = input("Digite o nome do produto 3: ")
preco_unitario3 = float(input("Digite o preço unitário do produto 3: "))
quantidade3 = int(input("Digite a quantidade do produto 3: "))

# Calcula o preço total de cada produto
total_produto1 = preco_unitario1 * quantidade1
total_produto2 = preco_unitario2 * quantidade2
total_produto3 = preco_unitario3 * quantidade3

# Calcula o preço total da compra
preco_total = total_produto1 + total_produto2 + total_produto3


print("Total: R${}".format(preco_total))
