ano = int(input('\033[36mDigite um ano: \033[m'))
if ano % 400 == 0:
    print('\033[32mO ano \033[m\033[36m{}\033[m\033[32m é um ano bissexto!\033[m'.format(ano))
else:
    if ano % 4 == 0 and ano % 100 != 0:
      print('\033[32mO ano \033[m\033[36m{}\033[m\033[32m é um ano bissexto!\033[m'.format(ano)) 
    else:
        print('\033[32mO ano \033[m\033[36m{}\033[m\033[32m não é um ano bissexto!\033[m'.format(ano)) 
