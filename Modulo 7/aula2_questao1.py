# Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso. 
# Dica: usando listas você não precisa fazer um "if" para cada mês.
# Ex:
# Digite uma data de nascimento: 29/10/1973
# Você nasceu em  29 de Outubro de 1973.

def imprimir_data_por_extenso():
    data = input('Digite uma data de nascimento (dd/mm/aaaa): ')
    dia, mes, ano = data.split("/")
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
             "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    mes_por_extenso = meses[int(mes) - 1]
    print('Você nasceu em {} de {} de {}.'.format(dia, mes_por_extenso, ano))

imprimir_data_por_extenso()
