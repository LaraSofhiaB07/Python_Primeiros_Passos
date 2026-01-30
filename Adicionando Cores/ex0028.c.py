from random import randint 
n1 = int(input('\033[34mDigite um número aleatório até 5: \033[m'))
computador = randint(0,5)
if (n1 == computador)  :
        print('\033[32mParabéns voçê acertou! Eu escolhi o número \033[m\033[34m{}\033[m\033[32m também!'.format(computador))
else:
        print('\033[31mVoçê errou! Eu escolhi o número \033[m\033[34m{}\033[m'.format(computador))
      