num = int(input('\033[4;32mInforme um número: \033[m'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('\033[34mAnalisando o número \033[m\033[32m{}\033[m'.format(num))
print('\033[31mUnidade: \033[m\033[32m{}\033[m'.format(u))
print('\033[31mDezena: \033[m\033[32m{}\033[m'.format(d))
print('\033[31mCentena: \033[m\033[32m{}\033[m'.format(c))
print('\033[31mMilhar: \033[m\033[32m{}'.format(m))
