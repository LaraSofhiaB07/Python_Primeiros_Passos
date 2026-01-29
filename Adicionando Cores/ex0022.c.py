from time import sleep
nome = str(input('\033[32mDigite seu nome completo: \033[m')).strip()
print('\033[34mAnalisando seu nome...\033[m')
sleep(2)
print('\033[36mSeu nome em letras maiúsculas é \033[m\033[32m{}\033[m'.format(nome.upper()))
print('\033[34mSeu nome em letras minúsculas é \033[m\033[32m{}\033[m'.format(nome.lower()))
print('\033[36mSeu nome teu ao todo \033[m\033[32m{}\033[m\033[36m letras'.format(len(nome) - nome.count(' ')))
separa= nome.split()
print('\033[34mSeu primeiro nome é \033[m\033[32m{}\033[m\033[34m e ele tem \033[m\033[32m{}\033[m\033[34m letras\033[m'.format(separa[0], len(separa[0])))