# Exercício 11 – Situação do aluno (nota + presença)
# Peça:
# - nota final (0 a 10);
# - porcentagem de presença (0 a 100).
# Regras para aprovação: nota ≥ 7 e presença ≥ 75.
# Se não for aprovado, mostre o motivo:
# - "Reprovado por falta." se nota ≥ 7 e presença < 75;
# - "Reprovado por nota." se nota < 7 e presença ≥ 75;
# - "Reprovado por nota e falta." se nota < 7 e presença < 75.

nota = float(input("Insira Nota: "))
presenca = int(input("Quanto % de presença? (Insira apenas em valor inteiro): "))

if nota >= 7 and presenca >= 75:
    print(f"Aprovado com nota {nota} e presença {presenca}")
elif nota >= 7 and presenca < 75:
    print("Reprovado por falta ")
elif nota < 7 and presenca >= 75:
    print("Reprovado por Nota")
elif nota < 7 and presenca < 75:
    print("Reprovado por falta e nota")
