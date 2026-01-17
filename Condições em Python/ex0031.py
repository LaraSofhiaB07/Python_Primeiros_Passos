distancia = float(input('Qual é a distância da viagem em Km: '))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('Então o preço total será {}'.format(preço))