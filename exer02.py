# Exercício 2 – Número par ou ímpar
# Peça um número inteiro ao usuário e mostre se ele é:
# - "Par";
# - ou "Ímpar".

num1 = int(input("Digite um número inteiro: "))

if (num1 % 2 == 0):
    print("O número é par")
else:
    print("O número é ímpar")