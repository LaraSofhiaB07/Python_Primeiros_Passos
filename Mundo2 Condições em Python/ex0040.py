n1=float(input('Primeira nota do aluno: '))
n2=float(input('Segunda nota do aluno: '))
média=(n1 + n2) /2
if média < 5.00:
   print('Está abaixo da média. REPROVADO!')
elif média == 5.00 or média < 6.9:
   print('Está de RECUPERAÇÃO!')
elif média == 7.00 or média > 7.00:
   print('Parabéns, está APROVADO!')