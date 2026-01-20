# Exercício 4 – Média de 3 notas
# Peça 3 notas (0 a 10), calcule a média e mostre:
# - "Aprovado" se média ≥ 7;
# - "Recuperação" se média entre 5 e 7;
# - "Reprovado" se média < 5.
# Mostre também a média calculada

nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))

media = (nota1 + nota2 + nota3) / 2

if (media >= 7):
    print("Aprovado")
elif (media > 5 and media < 7):
    print("Recuperação")
elif (media < 5):
    print("Reprovado")

print(f"Média calculada: {nota1} + {nota2} + {nota3} / 2 = {media}")
