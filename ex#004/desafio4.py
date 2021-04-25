print('===== DESAFIO 04 =====')
valor = input('Digite algo: ')

print('o valor é um texto:',valor.isalpha())
print('o valor é numérico:',valor.isnumeric())
print('o valor é alfanumérico:',valor.isalnum())
print('o valor da string é um número:',valor.isdigit())
print('o valor está em minúsculo:',valor.islower())
print('o valor está em maiúsculo:',valor.isupper())
print('o valor contém a primeira letra de cada palavra em maiúscula:',valor.istitle())
print('o valor pode ser imprimido:',valor.isprintable())

if valor.isspace():
    print('o valor é vazio:',valor.isispace())
else:
    print('o valor NÃO é vazio !!!')

if valor.isidentifier():
    print('o valor da string começa com qualquer caractere do alfabeto, seguido de caracteres de letras ou números:',valor.isidentifier())
else:
    print('o valor da string NÃO começa com qualquer caractere do alfabeto, seguido de caracteres e letras ou números')
