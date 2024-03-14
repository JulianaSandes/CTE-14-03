#1º exemplo:
numero = float(round(3.3224, 2))
print('O número com duas casas decimais é',numero,'.')
print('O número com duas casas decimais é '+str(numero)+'.')
print('O número com duas casas decimais é',str(numero)+'.')

#2º exemplo:
numero = 3.3224
print("O número com duas casas decimais é %.2f." %numero)

#3º exemplo:
numero = 3.3224
print('O número com duas casas decimais é {:.2f}.'.format(numero))

#4º exemplo:
numero = 3.3224
print(f"O número com duas casas decimais é {numero:.2f}.")
