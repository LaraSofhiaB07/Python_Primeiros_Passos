medida = float(input('\033[7m Uma distância em metros: \033[m'))
cm = medida * 100
mm = medida * 1000
print('\033[32mA media de\033[m \033[4;36m{}m\033[m \033[32mcorresponde a\033[m \033[4;36m{:.0f}cm\033[m\033[32m e\033[m\033[4;36m {:.0f}mm\033[m'.format(medida, cm, mm))