n = int(input('\033[4;36mDigite um número:\033[m'))
print('\033[35m O dobro de\033[m \033[31m {}\033[m \033[35m vale \033[m \033[31m{}.\033[m'.format(n, (n*2)))
print('\033[32m O triplo de \033[m \033[31m{} \033[m \033[32mvale\033[m \033[31m {}\033[m \033[33m. \n A raiz quadrada de \033[m \033[31m{}\033[m \033[33m é igual a\033[m \033[31m {:.2f}.\033[m'.format(n, (n*3), n, pow(n, (1/2))))