from adivinhe import jogoNumeroVer2, jogoNumero
from forca import gg
import titulos
from os import system

print('*' * 60)
print(' Escolha seu Game '.center(60, '-'))
print('*' * 60)

print('\n(1) Forca \n(2) Adivinhe o número')
jogo = int(input('Qual vai ser o game? '))


def escolher_jogo():
     
    if (jogo == 1):
        titulos.forca()
        gg()
    elif (jogo == 2):
        while True:
            try:
                x = input("Deseja jogar a versão 1 ou 2 ?")
                break
            except:
                print("Digite apenas 1 ou 2")
        if x == '1':
            titulos.numero1()
            jogoNumero()
        else:
            titulos.numero2()
            jogoNumeroVer2()

if __name__ == '__main__':
    while True:
        system('cls')
        escolher_jogo()
        dale = input("Deseja jogar novamente? digite 'SIM' ou qualquer tecla para sair.")
        if dale.upper() != 'SIM':
            exit()
        else:
            jogo = int(input("Qual vai ser o proximo game ?\n(1) Forca \n(2) Adivinhe o número\n:"))
            system("cls")