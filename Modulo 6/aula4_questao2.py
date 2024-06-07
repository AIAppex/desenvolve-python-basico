# Solicite uma frase do usuário e usando compreensão de listas imprima:
# A lista de vogais da frase, ordenada alfabeticamente
# A lista de consoantes da frase
# Exemplo:
# Digite uma frase: Eu gosto de programar em Python
# Vogais: ['a', 'a', 'e', 'e', 'o', 'o', 'o', 'o', 'u']
# Consoantes: ['E', 'g', 's', 't', 'd', 'p', 'r', 'g', 'r', 'm', 'r', 'm', 'P', 'y', 't', 'h', 'n']

def separar(frase):
    vogais = sorted([letra for letra in frase if letra.lower() in 'aeiou'])
    consoantes = [letra for letra in frase if letra.isalpha() and letra.lower() not in 'aeiou']
    return vogais, consoantes

frase = input('Digite uma frase: ')
vogais, consoantes = separar(frase)
print('Vogais:', vogais)
print('Consoantes:', consoantes)
