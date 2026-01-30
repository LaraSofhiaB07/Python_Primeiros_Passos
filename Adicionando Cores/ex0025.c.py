nome = str(input('\033[4;32mQual é seu nome completo? \033[m')).strip()
print('\033[36mSeu nome tem Silva? \033[m\033[31m{}\033[m'.format('silva' in nome.lower()))