#Calculadora simples
print("Bem vindo a Calculadora")
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
tipodecalculo = input("Digite o formato do calculo (+,-,*,/): ")
#adicionar if e elif a cada tipo de calculo
if tipodecalculo == "+":
    resposta = valor1 + valor2
elif tipodecalculo == "/":
    if valor2 != 0:
        resposta = valor1 / valor2
    else:
        resposta = "Erro de calculo"
elif tipodecalculo == "*":
    resposta = valor1 * valor2
elif tipodecalculo == "-":
    respota = valor1 - valor2
else:
    resposta = "numeros invalidos"
print("O calculo dos numeros são: ", resposta) 

