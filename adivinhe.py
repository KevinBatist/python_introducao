def jogoNumero():

    import random

    print("\nVocê terá 3 tentativas para acertar.".center(60," "))
 
    numero = random.randint(0, 2)
    jogadas = 0

    while True :
        try:
            tentativa = int(input("\nDigite o seu palpite: "))
            print(f"Jogada número {jogadas+1}".center(60, "-"))
            print(f"Seu palpite foi: {tentativa:02d}")
        except:
            print("Digite apenas numeros inteiros.")
            continue
        else:
        
            acerto = numero == tentativa
            maior = tentativa > numero
            menor = tentativa < numero

            if acerto:
                print("Parabéns você acertou!!!")
                break
            else:
                if maior:
                    print("\nSeu chute foi maior que o numero secreto")
                else:
                    print("\nSeu chute foi menor que o numero secreto")

            x = input("\nDigite 'EXIT' para sair, ou qualquer tecla para continuar: ")

            if x.upper() == "EXIT":
                print("Saindo do jogo")
                exit()
            else:
                jogadas += 1
                # print(f"Jogada número {jogadas} efetuada".center(60, "^"))

                if jogadas == 3:
                    print(f"\n\n*Voce atingiu o numero máximo {jogadas} de tentativas*\nFIM DE JOGO.")
                    exit()

def jogoNumeroVer2():
    import random

    print('***************************************')
    print('****** Adivinhe qual é o número! ******')
    print('***************************************')

    numero_secreto = random.randrange(0,101)
    total_tentativas = 0
    pontos = 1000

    print('Qual o nível de dificuldade?')
    print('(1) Padawan \n(2) Cavalheiro \n(3) Mestre Jedi')

    nivel = int(input('\nDefina o nível: '))

    if(nivel == 1):
        total_tentativas = 20
    elif(nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    pontos_a_perder = int(pontos / total_tentativas)
    print('Sua pontuação atual: {}' . format(pontos))

    for rodada in range(1, total_tentativas + 1):
        print('\nTentativa {:02d} de {:02d}' . format(rodada, total_tentativas))
        tentativa = int(input('Tente acertar o número entre 1 e 100: '))
        print('Você digitou: ', tentativa)

        if (tentativa < 1 or tentativa > 100):
            print('Tentativa INVÁLIDA! Somente números entre 1 e 100!')
            continue

        acerto = tentativa == numero_secreto
        ehmaior = tentativa > numero_secreto
        ehmenor = tentativa < numero_secreto

        if acerto:
            print('Boa tentativa. ACERTOU!!!! Fez {} pontos' . format(pontos))
            break 
        else:
            pontos_proximidade = 50 - abs(numero_secreto - tentativa)
            pontos = (pontos - pontos_a_perder + pontos_proximidade)
            print('Não foi dessa vez. ERROU!!!!')
            if ehmaior:
                print('Sua tentativa foi MAIOR que o número secreto.')
            elif ehmenor:
                print('Sua tentativa foi MENOR que o número secreto.')
            if(rodada < total_tentativas):
                print('Sua pontuação atual: {}' . format(pontos))
            else:
                print('\n------------------------------------')
                print('O número secreto era {}' . format(numero_secreto))
                print('Sua pontuação FINAL: {}' . format(pontos))
                print('GAME OVER')
                print('------------------------------------')
        
    print('Obrigado por participar')
