larg = float(input('\033[4;31;44mLargura da parede: \033[m'))
alt = float(input('\033[4;34;41mAltura da parede: \033[m'))
área = larg * alt 
print('\033[33mSua parede tem a dimensão de\033[m \033[31m{} x {}\033[m \033[33me sua área é de \033[m\033[31m{}m².\033[m'.format(larg, alt, área))
tinta = área / 2
print('\033[34mPara pintar essa parede, você precisará de \033[m\033[31m{}l\033[34m de tinta.\033[m'.format(tinta))