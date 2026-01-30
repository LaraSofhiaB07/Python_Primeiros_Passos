frase = str(input('\033[34mDigite uma frase: \033[m')).upper().strip()
print('\033[32mA letra A aparece \033[m\033[31m{}\033[m\033[32m vezes na frase\033[m'.format(frase.count('A')))
print('\033[32mA primeira letra A apareceu na posição \033[m\033[31m{}\033[m'.format(frase.find('A')+1))
print('\033[32mA última letra A apareceu na posição \033[m\033[31m{}\033[m'.format(frase.rfind('A')+1))
