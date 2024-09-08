todasas_notas = 0
total_notas = 0

while True:
    nota = float(input("Digite uma nota, ou -1 para finalizar:  "))

    if nota == -1:
        break
    
    todasas_notas += nota
    total_notas += 1
if total_notas > 0:
    media = todasas_notas / total_notas
    print(f"A média das notas é: {media:.2f}")
else:
    print("Nenhuma nota foi inserida.")
