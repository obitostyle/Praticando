nota1 = float(input("Digite a primeira nota (peso 2): "))
nota2 = float(input("Digite a segunda nota (peso 3): "))
nota3 = float(input("Digite a terceira nota (peso 5): "))

media_ponderada = (nota1 * 2 + nota2 * 3 + nota3 * 5) / (2 + 3 + 5)

print(f"A média do aluno é: {media_ponderada:.2f}")
