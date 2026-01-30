salario = float(input('\033[32mQual é o valor do seu salário?: \033[m'))
if salario > 1250 :
    salario *= 1.10
    print('\033[34mSeu salário com o aumento de 10% será \033[m\033[32m{:.2f}\033[m'.format(salario))
else:
    if salario <= 1250 : 
        salario *= 1.15
        print('\033[34mSeu salário como aumento de 15% será \033[m\033[32m{:.2f}\033[m'.format(salario))

