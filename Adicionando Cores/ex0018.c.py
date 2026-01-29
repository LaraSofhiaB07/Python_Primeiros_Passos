from math import radians, sin, cos, tan
ângulo = float(input('\033[32mDigite o ângulo que voçê deseja: \033[m'))
seno = sin(radians(ângulo))
print('\033[34mO ângulo de \033[m\033[32m{}\033[m\033[34m tem o SENO de \033[m\033[31m{:.2f}.\033[m'.format(ângulo, seno))
cosseno = cos(radians(ângulo))
print('\033[34mO ângulo de \033[m\033[32m{}\033[m\033[34m tem o COSSENO de \033[m\033[31m{:.2f}.\033[m'.format(ângulo, cosseno))
tangente = tan(radians(ângulo))
print('\033[34mO ângulo de \033[m\033[32m{}\033[m\033[34m tem a TANGENTE de \033[m\033[31m{:.2f}.\033[m'.format(ângulo, tangente))