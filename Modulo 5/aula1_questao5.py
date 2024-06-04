# Você está trabalhando em um sistema de mensagens instantâneas, que deve permitir o uso de emojis nas conversas entre pessoas.

import emoji

print("Emojis disponíveis:")
print("❤️ - :red_heart:")
print("👍 - :thumbs_up:")
print("🤔 - :thinking_face:")
print("🥳 - :partying_face:")

frase_code = input(" Digite uma frase e ela será emojizada: ")

frase_final = emoji.emojize(frase_code, delimiters=(':', ':'))

print("Frase emojizada:")
print(frase_final)