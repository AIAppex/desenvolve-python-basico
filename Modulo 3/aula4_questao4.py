# 4) Você está implementando um sistema de entrega expressa e precisa calcular o valor do frete com base na distância e no peso do pacote. Escreva um código que solicita a distância da entrega em quilômetros e o peso do pacote em quilogramas. O programa deve calcular e imprimir o valor do frete de acordo com as seguintes regras:
# Distância até 100 km: R$1 por kg.
# Distância entre 101 e 300 km: R$1.50 por kg.
# Distância acima de 300 km: R$2 por kg.
# Acrescente uma taxa de R$10 para pacotes com peso superior a 10 kg

def calcular_frete(distancia_km, peso_kg):
    
    if peso_kg > 10:
        taxa_adicional = 10
    else:
        taxa_adicional = 0

    
    if distancia_km <= 100:
        valor_frete = peso_kg * 1
    elif 101 <= distancia_km <= 300:
        valor_frete = peso_kg * 1.5
    else:
        valor_frete = peso_kg * 2

   
    valor_total = valor_frete + taxa_adicional

    return valor_total


distancia_entrega = float(input("Digite a distância da entrega em quilômetros: "))
peso_pacote = float(input("Digite o peso do pacote em quilogramas: "))


valor_total_frete = calcular_frete(distancia_entrega, peso_pacote)


print("O valor do frete é R${}".format(valor_total_frete))

