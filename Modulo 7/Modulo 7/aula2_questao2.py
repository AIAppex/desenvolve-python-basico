# Desenvolva um programa que solicite ao usuário inserir uma frase e substitua todas as ocorrências de vogal por "*".
# Ex:
# Digite uma frase: O rato roeu a roupa do rei
# Frase modificada: * r*t* r*** * r**p* d* r**

def substituir_vogais():
    frase = input('Digite uma frase: ')
    vogais = 'aeiouAEIOU'
    for vogal in vogais:
        frase = frase.replace(vogal, '*')
    print('Frase modificada: ', frase)

substituir_vogais()
