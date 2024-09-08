frase = input("Digite uma palavra ou frase: ")
frase_inteira = ''.join(frase.lower().split())
if frase_inteira== frase_inteira[::-1]:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")