# Exercício 12 – IMC (Índice de Massa Corporal)
# Peça:
# - peso (kg);
# - altura (m).
# Calcule IMC = peso / (altura * altura).
# Depois mostre:
# - IMC < 18.5 → "Abaixo do peso";
# - 18.5 a 24.9 → "Peso normal";
# - ≥ 25 → "Acima do peso".
# Mostre também o valor do IMC calculado.

peso = float(input("Insira peso (Apenas números): "))
altura = float(input("Insira Altura (Apenas números. ex: x.xx): "))

imc = peso / (altura * altura)

if imc < 18.5:
    print(f"Abaixo do peso ({imc})")
elif imc > 18.5 and imc < 24.9:
    print(f"Peso normal ({imc})")
elif imc >= 25:
    print(f"Acima do peso ({imc})")