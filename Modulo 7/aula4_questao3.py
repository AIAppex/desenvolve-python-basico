# Baixe o arquivo contendo o roteiro do filme brasileiro "Estômago" (link a seguir) e salve em seu computador com o nome "estomago.txt". 

# Link: https://aplauso.imprensaoficial.com.br/edicoes/12.0.813.502/12.0.813.502.txt

# Em seguida crie um script em Python que abra o arquivo para leitura e imprima: 
# O texto das primeiras 25 linhas
# O número de linhas do arquivo
# A linha com maior número de caracteres
# O número de menções aos nomes dos personagens "Nonato" e "Íria" (inclua todas as variações de maiúsculas e minúsculas e atenção para não incluir a substring "iria" se ela fizer parte de outras palavras).

import re

with open("estomago.txt", 'r') as f:
    lines = f.readlines()

print("Primeiras 25 linhas:")
for line in lines[:25]:
    print(line.strip())

print(f"\nNúmero de linhas: {len(lines)}")

max_length_line = max(lines, key=len)
print(f"\nLinha com maior número de caracteres: {max_length_line.strip()}")

nonato_count = sum(len(re.findall(r'\bNonato\b', line, re.I)) for line in lines)
iria_count = sum(len(re.findall(r'\bÍria\b', line, re.I)) for line in lines)
print(f"\nNúmero de menções a 'Nonato': {nonato_count}")
print(f"Número de menções a 'Íria': {iria_count}")
