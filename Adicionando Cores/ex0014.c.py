c = float(input('\033[31mInforme a temperatura em °C:\033[m'))
f = 9 * c / 5 + 32
print ('\033[32mA temperatura de \033[m\033[36m{}°C\033[m\033[32m corresponde a \033[m\033[36m{} °F!\033[m'.format(c, f))