distancia = float(input('\033[33mQual é a distância da viagem em Km: \033[m'))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('\033[33mEntão o preço total será de \033[m\033[32mR${}\033[m'.format(preço))