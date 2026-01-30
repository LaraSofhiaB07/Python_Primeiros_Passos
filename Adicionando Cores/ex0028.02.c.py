from random import randint
from time import sleep
computador = randint(0, 5)  
print('\033[33m-=-\033[m' * 20)
print('\033[34mVou pensar em um número entre 0 e 5. Tente adivinhar...\033[m')
print('\033[33m-=-\033[m' * 20)
jogador = int(input('\033[34mEm que número eu pensei? \033[m'))
print('\033[33mPROCESSANDO...\033[m')
sleep(2) 
if jogador == computador:
    print('\033[32mPARABÉNS! Você conseguiu me vencer!\033[m')
else:
    print('\033[31mGANHEI! Eu pensei no número \033[m\033[32m{}\033[m\033[31m e não no \033[m\033[32m{} \033[m\033[31m!\033[m'.format(computador, jogador))
