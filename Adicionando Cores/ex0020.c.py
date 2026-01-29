from random import shuffle 
n1 = str(input('\033[31;47mPrimeiro aluno: \033[m'))
n2 = str(input('\033[32;47mSegundo aluno : \033[m'))
n3 = str(input('\033[34;47mTerceiro aluno: \033[m'))
n4 = str(input('\033[35;47mQuarto aluno  : \033[m'))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('\033[33;47mA ordem de apresentação será: \033[m{}{}{}\033[33m!!!'.format('\033[4;34m', lista, '\033[m'))

