salario = float(input('Qual é o valor do seu salário?: '))
if salario > 1250 :
    salario *= 1.10
    print('Seu salário com o aumento de 10% será {:.2f}'.format(salario))
else:
    if salario <= 1250 : 
        salario *= 1.15
        print('Seu salário como aumento de 15% será {:.2f}'.format(salario))

