texto = str(input("Digite uma frase ")).casefold()

letra = str(input("Digite uma letra ")).casefold()

contagem = texto.count(letra)

print(f"A letra apareceu {contagem} vezes.")
