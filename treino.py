palavra = "SALVE"
list_palavra = list(palavra)
resposta = ["_"] * len(palavra)
erros = 0

while True:
    x=0
    tentativa = input("Digite uma letra: ")
    for index, letra in enumerate(list_palavra):
        if letra.upper() == tentativa.upper():
            resposta[index] = letra
            x=1

    print(resposta)

    if "_" not in resposta:
        print("Parabéns, você acertou a palavra!")
        break
    else:
        erros += 1
        if x==0:
            print("Erros cometidos: ", erros)
        if erros == 11:
            print("Você excedeu o limite de erros. A palavra era: ", palavra)
            break
