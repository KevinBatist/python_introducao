import random


def titulo():
    print("*" * 40)
    print(" Jogo da forca ".center(40,"-"))
    print("*" * 40)


def carrega_palavra():
    arquivo = open("frutas.txt", 'r')
    palavras = []

    for i in arquivo:
        i = i.strip()
        palavras.append(i.strip())


    arquivo.close()
    sorteio = random.randint(0,len(palavras))

    return(palavras[sorteio].upper())
    

def forca():
    titulo()
        
    palavra_secreta = carrega_palavra()
    lista_secreta = list(palavra_secreta)
    letras_acertadas = ['_'] * len(palavra_secreta)

    morreu = False
    acertou = False
    erros = 0

    while(not morreu and not acertou):
        tentativa = input('Qual a letra? ').strip().upper()

        if tentativa in lista_secreta and tentativa not in letras_acertadas:
            for index, letra in enumerate(lista_secreta):

                if (tentativa == letra):
                    letras_acertadas[index] = letra.upper()
                    erros = 0

            print(letras_acertadas)
            
        else:
            erros += 1
            morreu = erros == 3

        if "_" not in letras_acertadas:
            acertou = True

    if acertou:
        print("Voce venceu!")
    else:
        print("Voce perdeu!")
        print("A palavra era:", palavra_secreta)


    print("GG Forca")
    print('\nObrigado por participar!\n')

if __name__ == "__main__":
    forca()
