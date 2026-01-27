salário = float(input('\033[34;42mQual é o salário do funcionário? R$ \033[m'))
novo = salário + (salário * 15 / 100)
print ('\033[34mUm funcionário que ganhava \033[m\033[31mR${:.2f}\033[m\033[34m, com 15% de aumento, passa a receber\033[m\033[31m R${:.2f}\033[m'.format(salário, novo))