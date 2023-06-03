def jogoNumero():

    import random

    titulo = ("Adivinhe qual o número")
    print(titulo.center(len(titulo)+10, "*"))
    print("\nVocê terá 3 tentativas para acertar.")
    print("-".center(60, '-'))
    numero = random.randint(0, 2)
    jogadas = 0

    while True :
        try:
            tentativa = int(input("\nDigite o seu palpite: "))
        except:
            print("Digite apenas numeros inteiros.")
            continue
        else:
        
            acerto = numero == tentativa
            maior = tentativa > numero
            menor = tentativa < numero

            if acerto:
                print("\nParabéns você acertou!!!")
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
                print(f"Jogada número {jogadas} efetuada".center(60, "^"))

                if jogadas == 3:
                    print("\n\n*Voce atingiu o numero máximo de tentativas*\nFIM DE JOGO.")
                    exit()

