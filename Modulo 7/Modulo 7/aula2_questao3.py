# Desenvolva um programa que verifique se uma frase fornecida pelo usuário é um palíndromo (ou seja, lida da mesma forma de trás para frente). Ignore espaços em branco ou sinais de pontuação, e considere maiúsculas e minúsculas da mesma forma. Seu programa deve continuar rodando até que o usuário digite "Fim".Ex:

# Digite uma frase (digite "fim" para encerrar): Radar
# "Radar" é palíndromo
# Digite uma frase (digite "fim" para encerrar): Bom dia!
# "Bom dia!" não é palíndromo
# Digite uma frase (digite "fim" para encerrar): Ame o poema
# "Ame o poema" é palíndromo
# Digite uma frase (digite "fim" para encerrar): A Daniela ama a lei? Nada!
# "A Daniela ama a lei? Nada!" é palíndromo
# Digite uma frase (digite "fim" para encerrar): fim

import re

def verificar_palindromo():
    while True:
        frase = input('Digite uma frase (digite \'fim\' para encerrar): ')
        if frase.lower() == "fim":
            break
        else:
            frase_limpa = re.sub(r'\W+', '', frase).lower()
            if frase_limpa == frase_limpa[::-1]:
                print("\"{}\" é palíndromo".format(frase))
            else:
                print("\"{}\" não é palíndromo".format(frase))

verificar_palindromo()
