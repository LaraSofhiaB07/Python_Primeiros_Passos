from math  import trunc
num = float(input('\033[4;31mDigite um valor:\033[m'))
print('\033[32mO valor digitado foi \033[m\033[31m{}\033[m\033[32m e a sua porção inteira é \033[m\033[31m{}\033[m'.format(num, trunc(num))) 