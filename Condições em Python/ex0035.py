r1 = int(input('Primeira reta -> comprimento: '))
r2 = int(input('Segunda reta -> comprimento: '))
r3 = int(input('Terceira reta -> comprimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3:
        print('Com essas retas {}, {} e {}, podem se formar um triângulo e é um Triângulo equilátero'.format(r1,r2,r3))
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Com essas retas {}, {} e {}, podem se formar um triângulo e é Triângulo isósceles'.format(r1,r2,r3))
    else:
        print('Com essas retas {}, {} e {}, podem se formar um triângulo e é Triângulo escaleno'.format(r1,r2,r3))
else:
    print('Com essas retas {},{} e {}, Não forma um triângulo'.format(r1,r2,r3))
