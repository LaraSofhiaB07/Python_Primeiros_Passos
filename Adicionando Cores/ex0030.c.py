número = int(input('\033[4;36mDigite qualquer número: \033[m'))
if número % 2 == 0:
    print("\033[4;34mO número \033[m\033[4;36m{}\033[m\033[4;34m é PAR.\033[m".format(número)) 
else:
    print("\033[4;34mO número \033[m\033[4;36m{}\033[m\033[4;34m é ÍMPAR.\033[m".format(número))