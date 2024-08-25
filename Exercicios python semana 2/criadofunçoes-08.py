def escrevaumnumero(numero):
    if numero % 2 == 0:
        return print("Este numero é par")
    else: 
        return print("Esté numero é impar")
num=int(input("Digite um numero para ver se ele é par ou impar"))
escrevaumnumero(num)