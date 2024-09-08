# Solicita um número ao usuário
numero = int(input("Digite um número: "))

soma_divisores = sum(i for i in range(1, numero) if numero % i == 0)

if soma_divisores == numero:
    print(f"O número {numero} é perfeito.")
else:
    print("O número não é perfeito.")
