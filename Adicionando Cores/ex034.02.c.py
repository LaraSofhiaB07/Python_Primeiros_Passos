salario = float(input('\033[32mQual é o salário do funcionário? R$\033[m'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('\033[36mQuem ganhava \033[m\033[31mR${:.2f}\033[m\033[36m passa a ganhar \033[m\033[32mR${:.2f}\033[m\033[36m agora.\033[m'.format(salario, novo))
