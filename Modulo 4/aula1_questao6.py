# Exercício de maratona: https://www.beecrowd.com.br/judge/pt/problems/view/1094
# Maria precisa de sua ajuda para organizar os experimentos de seu laboratório. Ela quer saber no final do ano, quantas cobaias foram utilizadas no laboratório e o percentual de cada tipo de cobaia utilizada. Este laboratório utiliza três tipos de cobaias: sapos, ratos e coelhos. 
# Entrada: A primeira linha de entrada é um inteiro N com a quantidade de experimentos registrados. As N linhas seguintes contém um inteiro Quantia que representa a quantidade de cobaias utilizadas e um caractere Tipo ('S', 'R' ou 'C') com o tipo de cobaia (S:Sapo, R:Rato ou C:Coelho).
# Saída: Apresente o total de cobaias utilizadas, o total de cada tipo de cobaia e o percentual de cada uma em relação ao total de cobaias utilizadas

N = int(input('Digite a quantidade de experimentos registrados: '))
total_cobaias = 0
total_sapos = 0
total_ratos = 0
total_coelhos = 0

while N > 0:
    entrada = input('Digite a quantidade e o tipo de cobaia (S, R ou C): ')
    quantia, tipo = entrada.split()
    quantia = int(quantia)

    total_cobaias += quantia

    if tipo == 'S':
        total_sapos += quantia
    elif tipo == 'R':
        total_ratos += quantia
    elif tipo == 'C':
        total_coelhos += quantia

    N -= 1

percentual_sapos = (total_sapos / total_cobaias) * 100
percentual_ratos = (total_ratos / total_cobaias) * 100
percentual_coelhos = (total_coelhos / total_cobaias) * 100

print('Total de cobaias utilizadas: {}'.format(total_cobaias))
print('Total de sapos: {} ({}%)'.format(total_sapos, percentual_sapos))
print('Total de ratos: {} ({}%)'.format(total_ratos, percentual_ratos))
print('Total de coelhos: {} ({}%)'.format(total_coelhos, percentual_coelhos))