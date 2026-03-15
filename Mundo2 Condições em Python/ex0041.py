from datetime import date
atual = date.today().year
nasc = int(input('Digite seu ano de nascimento: '))
idade = atual - nasc
if idade < 9 :
    print('O atleta tem {} anos de idade.'.format(idade))
    print('Classificação: MIRIM')
elif idade >=9 and idade <=14:
    print('O atleta tem {} anos de idade.'.format(idade))
    print('Classificação: INFANTIL')
elif idade > 14 and idade <=19:
    print('O atleta tem {} anos de idade.'.format(idade))
    print('Classificação: JUNIOR')
elif idade >19 and idade <=25:
     print('O atleta tem {} anos de idade.'.format(idade))
     print('Classificação: SÊNIOR')
elif idade >25:
     print('O atleta tem {} anos de idade.'.format(idade))
     print('Classificação: MASTER')