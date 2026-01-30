from datetime import date
ano = int(input(' \033[34mQue ano quer analisar? Coloque 0 para analisar o ano atual:  \033[m'))
if ano == 0:
   ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
     print('\033[32mO ano \033[m\033[31m{}\033[m\033[32m é BISSEXTO \033[m'.format(ano))
else:
     print('\033[32mO ano \033[m\033[31m{}\033[m\033[32m NÃO é BISSEXTO\033[m'.format(ano))
