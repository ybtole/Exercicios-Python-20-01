# Exercício 8 – Conceito da nota
# Peça uma nota de 0 a 10 e converta para conceito:
# - 9 a 10 → conceito A;
# - 7 a 8.9 → conceito B;

nota = float(input("Insira uma nota: "))
print("9 a 10 -> Conceito A")
print("7 a 8.9 -> Conceito B")

if nota >= 9 and nota <= 10:
    print("Conceito A")
elif nota >= 7 and nota <= 8.9:
    print("Conceito B")

