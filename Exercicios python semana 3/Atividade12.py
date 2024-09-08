import random
#gerar um numero aleatorio
numero_aleatorio = random.randint(1,100)
tentativas = None
#Loop
while tentativas != numero_aleatorio:
    tentativas = int(input("Adivinhe o numero: "))
    if tentativas < numero_aleatorio:
        print("Maior")
    elif tentativas > numero_aleatorio:
        print("Menor")
    else:
        print("Parabéns você achou o numero")