from random import choice
n1 = str(input('\033[4;32mPrimeiro aluno: \033[m'))
n2 = str(input('\033[4;33mSegundo aluno: \033[m'))
n3 = str(input('\033[4;34mTerceiro aluno: \033[m'))
n4 = str(input('\033[4;35mQuarto aluno: \033[m'))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('\033[36mO aluno escolhido foi \033[m\033[31m{}\033[m'.format(escolhido))