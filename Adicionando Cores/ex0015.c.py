dias = int(input('\033[36;42mQuantos dias alugados? \033[m'))
km = float(input('\033[32;46mQuantos km rodados? \033[m'))
pago = (dias * 60) + (km * 0.15)
print('\033[34mO total a pagar é de \033[m\033[32mR${:.2f}\033[m'.format(pago))