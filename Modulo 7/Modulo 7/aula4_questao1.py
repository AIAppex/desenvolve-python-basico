# Escreva um script Python que solicita uma frase do usuário e a salve em um arquivo chamado "frase.txt" no mesmo local do seu script. Imprima em seguida o caminho completo do arquivo salvo.
# Ex: 
# Digite uma frase: Bom dia, meu nome é Davi.
# Frase salva em /Users/laranjeira/python-basico/frase.txt

import os

frase = input('Digite uma frase: ')
with open("frase.txt", "w") as arquivo:
    arquivo.write(frase)

caminho_completo = os.path.abspath("frase.txt")

print('Frase salva em {}'.format(caminho_completo))
