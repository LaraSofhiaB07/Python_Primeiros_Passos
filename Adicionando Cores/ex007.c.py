n1=int(input(('\033[4;31;44mDigite um valor:\033[m')))
n2=int(input('\033[4;34;41mDigite mais um valor:\033[m'))
s= n1+n2
m= n1 * n2 
d= n1 / n2
di= n1 // n2
e= n1 ** n2
print('\033[36mA soma é \033[m \033[4;31m{}\033[m \033[32m\nO produto é\033[m \033[4;31m{}\033[m \033[33m \nA divisão é\033[m \033[4;31m{:.3f}.\033[m'.format(s, m, d))
print('\033[35mDivisão inteira\033[m \033[4;31m {}\033[m \033[35m e potência\033[m \033[4;31m {}.\033[m'.format(di, e))