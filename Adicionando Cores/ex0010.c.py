real= float(input('\033[32mQuanto dinheiro você tem na carteira? R$\033[m'))
dolar = real/ 5.41
print('\033[34mCom R${:.2f} você pode comprar US${:.2f}\033[m'.format(real, dolar))