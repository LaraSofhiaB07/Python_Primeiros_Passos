print('\033[36m-=\033[m' * 20)
print('\033[35mAnalisador de Triângulos\033[m')
print('\033[36m-=\033[m' * 20)
r1 = float(input('\033[31mPrimeiro segmento: \033[m'))
r2 = float(input('\033[32mSegundo segmento: \033[m'))
r3 = float(input('\033[33mTerceiro segmento: \033[m'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[34mOs segmentos acima PODEM FORMAR triângulo\033[m')
else:
    print('\033[34mOs segmentos acima NÃO PODEM FORMAR triângulo\033[m')