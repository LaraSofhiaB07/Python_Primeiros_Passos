veloc = int(input('Qual a velocidade do carro? : '))
multa: int = (veloc-80) * 7
if veloc > 80:
    print('A velocidade do carro é {} Km, e voçê foi multado! E deve pagar um multa de R${} '.format(veloc,multa))
else:
    print('A velocidade do carro é {}, e está tudo certo! '.format(veloc))    