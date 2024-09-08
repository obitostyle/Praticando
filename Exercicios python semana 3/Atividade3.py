peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))
imc = peso / (altura ** 2)
print(f"Seu IMC é {imc:.2f}")