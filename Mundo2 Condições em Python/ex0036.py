casa = float(input('\033[32mValor da casa: R$ \033[m'))
salario = float(input('\033[35mSalário do comprador: R$ \033[m'))
anos = int(input('\033[33mQuantos anos de financiamento? \033[m'))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print('\033[36mPara pagar uma casa de R$ {:.2f} em {} anos,\033[m'.format(casa, anos))
print('\033[36ma prestação será de R$ {:.2f}\033[m'.format(prestacao))
if prestacao <= minimo:
    print('\033[32mEmpréstimo pode ser CONCEDIDO!\033[m')
else:
    print('\033[31mEmpréstimo NEGADO!\033[m')