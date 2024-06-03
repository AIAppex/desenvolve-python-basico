# 5) Solicite de um usuário seu gênero ("M" ou "F"), sua idade e seu tempo de serviço (em anos) e escreva uma expressão que imprima True se a pessoa já pode se aposentar, ou False caso contrário, de acordo com as seguintes regras:
# A: Para mulheres, ter mais de 60 anos. Para homens, 65.
# B: Ou ter trabalhado pelo menos 30 anos
# C: Ou ter 60 anos  e trabalhado pelo menos 25.

def pode_se_aposentar(genero, idade, tempo_servico):
    if genero.lower() == "f":
       
        return idade > 60 or (idade >= 60 and tempo_servico >= 25)
    elif genero.lower() == "m":
        
        return idade > 65 or tempo_servico >= 30
    else:
        
        return False


genero = input("Digite o gênero (M ou F): ")
idade = int(input("Digite a idade: "))
tempo_servico = int(input("Digite o tempo de serviço (em anos): "))

resultado = pode_se_aposentar(genero, idade, tempo_servico)
print("Pode se aposentar: {}".format(resultado))
