velocidade = float(input('\033[34;42mQual é a velocidade do carro? \033[m'))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('\033[33;41mMULTADO! Você excedeu o limite permitido.\033[m')
    print('\033[33;41mVocê deve pagar uma multa de R${:.2f}\033[m'.format(multa))
print('\033[32;44mTenha um bom dia! Dirija com segurança!\033[m')
