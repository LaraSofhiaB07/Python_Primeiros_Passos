preço = float(input('\033[33mQual é o preço do produto? R$\033[m'))
novo = preço - (preço * 5 / 100)
print ('\033[34mO produto que custava \033[32mR${:.2f}\033[m\033[34m, na promoção com desconto de 5% vai custar \033[m\033[32mR${:.2f}\033[m'.format(preço, novo)) 