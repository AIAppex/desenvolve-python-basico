# Escreva um script que leia o arquivo salvo no exercício anterior e salva em um novo arquivo "palavras.txt", removendo todos os espaços em branco e caracteres não alfabéticos, e separando cada palavra em uma linha. Ao final, imprima o conteúdo do arquivo "palavras.txt".
# Ex:
# Bom
# dia
# meu
# nome
# é
# D
# 
# avi

import re

with open("frase.txt", "r") as arquivo:
    frase = arquivo.read()

frase = re.sub(r'[^a-zA-ZáéíóúÁÉÍÓÚâêîôûÂÊÎÔÛãõÃÕçÇ\s]', '', frase)
palavras = frase.split()

with open("palavras.txt", "w") as arquivo:
    for palavra in palavras:
        arquivo.write(palavra + '\n')

with open("palavras.txt", "r") as arquivo:
    conteudo = arquivo.read()

print(conteudo)
