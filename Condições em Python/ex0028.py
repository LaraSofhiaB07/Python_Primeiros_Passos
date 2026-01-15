from random import randint 
n1 = int(input('Digite um número aleatório até 5: '))
computador = randint(0,5)
if (n1 == computador)  :
        print(' Parabéns voçê acertou! Eu escolhi o número {} também!'.format(computador))
else:
        print(' Voçê errou! Eu escolhi o número {}'.format(computador))
      
   
