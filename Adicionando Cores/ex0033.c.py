
n1 = int(input('\033[31mDigite o primeiro número: \033[m'))
n2 = int(input('\033[32mDigite o segundo número: \033[m'))
n3 = int(input('\033[33mDigite o terceiro número: \033[m'))
if n1 > n2 and n2 > n3 :
    print('\033[34mO maior número é {}, em segundo {} e por último {}\033[m'.format(n1, n2, n3))
else:
    if n1 > n3 and n3 > n2:
        print('\033[34mO maior número é {}, em segundo {} e por último {}\033[m'.format(n1, n3, n2))
    else:
        if n2 > n1 and n1 > n3:
            print('\033[34mO maior número é {}, em segundo {} e por último {}\033[m'.format(n2, n1, n3))
        else:
            if n2 > n3 and n3 > n1:
                print('\033[34mO maior número é {}, em segundo {} e por último {}\033[m'.format(n2, n3, n1))
            else:
                if n3 > n1 and n1 > n2:
                    print('\033[34mO maior número é {}, em segundo {} e por último {}\033[m'.format(n3, n1, n2))
                else:
                    if n3 > n2 and n2 > n1:
                        print('\033[34mO maior número é {}, em segundo {} e por último {}\033[m'.format(n3, n2, n1)) 
