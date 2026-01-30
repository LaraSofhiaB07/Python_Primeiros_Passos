r1 = int(input('\033[31mPrimeira reta -> comprimento: \033[m'))
r2 = int(input('\033[32mSegunda reta -> comprimento: \033[m'))
r3 = int(input('\033[33mTerceira reta -> comprimento: \033[m'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3:
        print('\033[34mCom essas retas \033[m\033[32m{}\033[m\033[34m,\033[m\033[32m {}\033[m\033[34m e \033[m\033[32m{}\033[m\033[34m, podem se formar um triângulo e é um \033[m\033[33mTriângulo equilátero\033[m'.format(r1,r2,r3))
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('\033[35mCom essas retas \033[m\033[32m{}\033[m\033[35m, \033[m\033[32m{}\033[m\033[35m e \033[m\033[32m{}\033[m\033[34m, podem se formar um triângulo e é um \033[m\033[33mTriângulo isósceles\033[m'.format(r1,r2,r3))
    else:
        print('\033[36mCom essas retas \033[m\033[32m{}\033[m\033[36m, \033[m\033[32m{}\033[m\033[36m e \033[m\033[32m{}\033[m\033[36m, podem se formar um triângulo e é um \033[m\033[33mTriângulo escaleno\033[m'.format(r1,r2,r3))
else:
    print('\033[31mCom essas retas \033[m\033[32m{}\033[m\033[31m, \033[m\033[32m{}\033[m\033[31m e \033[m\033[32m{}\033[m\033[31m, Não forma um triângulo\033[m'.format(r1,r2,r3))
