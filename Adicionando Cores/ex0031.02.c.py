print('\033[31mQual é a distância da sua viagem?: \033[m')
distancia = float(input())
print('\033[33mVocê está prestes a começar uma viagem de \033[m\033[31m{}Km.\033[m'.format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('\033[33mE o preço da sua passagem será de \033[m\033[32mR${:.2f}\033[m'.format(preço))

