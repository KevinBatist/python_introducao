from adivinhe import jogoNumeroVer2
from aforca import gg

print('****************************************')
print('---------- Escolha seu Game! -----------')
print('****************************************')

print('\n(1) Forca \n(2) Adivinhe o número')
jogo = int(input('Qual vai ser o game? '))

if (jogo == 1):
    print('GG forca')
    gg()
elif (jogo == 2):
    print('GG adivinhe')
    jogoNumeroVer2()
