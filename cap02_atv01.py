import random

titulo = ("Adivinhe qual o número")
print(titulo.center(len(titulo)+10, "*"))

numero = random.randint(0, 2)

jogadas = 1

print("Você tem 03 jogadas.\n")

#TA ERRADAO 

while jogadas <= 3:

    if jogadas == 1:
        try:
            tentativa = int(input(f"Digite um numero e tente acertar.\nJogada numero {jogadas:02d}: "))
        except:
            print("O jogo so funciona com numeros inteiros, inicie o programa novamente.")
            exit()        
    else:    
        tentativa = input("\nDigite outro numero para tentar novamente,\nou 'exit' para sair.\n\n>>>>>>>>>>>>:")

    maior = tentativa > numero
    menor = tentativa < numero
    acerto = tentativa == numero

    # print("\n", numero)
    
    if acerto:
        print("Parabens você digitou o numero correto!")
        print(f"Venceu na rodada: {jogadas:02d}")
        break
    else:
        if maior:
            print(f"Seu chute ({tentativa:02d}) foi maior que o numero secreto.")

        elif menor:
            print(f"Seu chute ({tentativa:02d}) foi menor que o numero secreto.")       
        jogadas += 1       
        
    if tentativa.upper() == "EXIT":
        print("Saindo do jogo.")
        exit()
    else:
        tentativa = int(tentativa)

    print(f"\nJogada numero {jogadas:02d}:")

print(f"Você atingiu o numero máximo de jogadas: ({jogadas:02d}).")
print("Saindo do jogo.")
