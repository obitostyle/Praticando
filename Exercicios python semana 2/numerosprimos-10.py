def é_primo(numero):
    if numero <=1:
        return False

    for i in range(2,int(numero ** 0.5) +1):
        if numero % i == 0:
            return False
        return True
print("Digite um numero inicial e final")
inicial = int(input("digite aqui o numero inicial: "))
final = int(input("Digite aqui o numero final: ")) 

for numero in range(inicial, final + 1):
    if é_primo(numero):
        print(numero)

