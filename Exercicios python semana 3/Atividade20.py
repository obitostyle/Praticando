# Inicializa a lista de números
numeros = []

# Solicita os números ao usuário
while True:
    numero = input("Digite um número (ou 'sair' para finalizar): ")
    
    if numero.lower() == 'sair':
        break
    else:
        numeros.append(float(numero))


if numeros:
    maior = max(numeros)
    menor = min(numeros)
    media = sum(numeros) / len(numeros)

    # Exibe o maior, o menor e a média
    print(f"Maior número: {maior}")
    print(f"Menor número: {menor}")
    print(f"Média dos números: {media:.2f}")
else:
    print("Nenhum número foi inserido.")
