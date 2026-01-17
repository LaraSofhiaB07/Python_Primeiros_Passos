n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
if n1 > n2 and n2 > n3 :
    print('O maior número é {}, em segundo {} e por último {}'.format(n1, n2, n3))
else:
    if n1 > n3 and n3 > n2:
        print('O maior número é {}, em segundo {} e por último {}'.format(n1, n3, n2))
    else:
        if n2 > n1 and n1 > n3:
            print('O maior número é {}, em segundo {} e por último {}'.format(n2, n1, n3))
        else:
            if n2 > n3 and n3 > n1:
                print('O maior número é {}, em segundo {} e por último {}'.format(n2, n3, n1))
            else:
                if n3 > n1 and n1 > n2:
                    print('O maior número é {}, em segundo {} e por último {}'.format(n3, n1, n2))
                else:
                    if n3 > n2 and n2 > n1:
                        print('O maior número é {}, em segundo {} e por último {}'.format(n3, n2, n1)) 
