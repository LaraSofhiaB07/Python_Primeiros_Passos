a = int(input('\033[34mPrimeiro valor: \033[m'))
b = int(input('\033[35mSegundo valor: \033[m'))
c = int(input('\033[36mTerceiro valor: \033[m'))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('\033[32mO menor valor digitado é \033[m\033[31m{}\033[m'.format(menor))
print('\033[32mO maior valor digitado é \033[m\033[31m{}\033[m'.format(maior))
