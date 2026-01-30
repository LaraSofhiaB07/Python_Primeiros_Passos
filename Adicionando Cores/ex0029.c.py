veloc = int(input('\033[32mQual a velocidade do carro? : \033[m'))
multa: int = (veloc-80) * 7
if veloc > 80:
    print('\033[34mA velocidade do carro é \033[m\033[31m{}\033[m\033[34mKm, e voçê foi multado! E deve pagar um multa de \033[m\033[32mR${}\033[m '.format(veloc,multa))
else:
    print('\033[34mA velocidade do carro é \033[m\033[31m{}Km\033[m\033[34m, e está tudo certo!\033[m'.format(veloc))    