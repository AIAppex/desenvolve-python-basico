# Escreva um programa em Python que utiliza a biblioteca datetime para exibir a data e hora atuais com a formatação apresentada a seguir:

from datetime import datetime

data = datetime.now().strftime('%d/%m/%y')
hora = datetime.now().strftime('%H:%M')

print('Date: {}'.format(data))
print('Time: {}'.format(hora))