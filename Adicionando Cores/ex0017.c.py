from math import hypot 
co = float(input('\033[4;34mComprimento do cateto oposto:\033[m'))
ca = float(input('\033[4;33mComprimento do cateto adiacente:\033[m'))
hi = hypot(co, ca)
print('\033[31mA hipotenusa vai medir \033[m\033[32m{:.2f}\033[m'.format(hi))