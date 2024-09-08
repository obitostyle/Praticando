
frase = input("Digite uma frase: ")

frase_invertida = ""

#Loop
for letra in frase:
    frase_invertida = letra + frase_invertida

# Exibe a frase invertida
print(f"A frase invertida é: {frase_invertida}")
