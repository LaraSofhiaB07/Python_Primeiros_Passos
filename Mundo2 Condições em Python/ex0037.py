numero = int(input("Digite um número qualquer inteiro: "))
print('Escolha qual será a base de conversão: ')
print(' 1- para Binário. ')
print(' 2- para octal. ')
print(' 3- para hexadecimal.')
base= int(input('Digite o número: '))
if base == 1 :
    print('O número {} convertido para BINÁRIO é igual a {}'.format(numero,(bin(numero)[2:]))) 
elif base == 2:
    print('O número {} convertido para OCTAL é igual a {}'.format(numero,(oct(numero)[2:]))) 
elif base == 3:
    print('O número {} convertido para HEXADECIMAL é igual a {}'.format(numero,(hex(numero)[2:])))
else:
    print('ERRO!, escolha a opção 1, 2 ou 3!')