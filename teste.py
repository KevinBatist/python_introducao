# import random

# #Diferença entre int e round, ignora a parte decimal
# numero = int(93.321321321)

# #Round arredonda de acordo com o decimal
# numero = round(93.76232132)

# #random gera um numero decimal entre 0 e 1, por isso multiplicamos por 100
# numero = int(random.random() * 100)

# #Gera um valor entre as referencias (inclui a primeira referencia)
# #METODO ORIGINAL
# numero = random.randrange(0,101,10)
# print(numero)

# #Gera um valor contento as referencias
# # = randrange b+1
# numero = random.randint(0,100)

word = "Salve"
guessed_word = ["_"] * len(word)

print(guessed_word)