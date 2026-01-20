# Exercício 7 – Frete de compra online
# Peça o valor de uma compra e calcule o frete:
# - valor < 50 → frete = 10;
# - 50 a 100 → frete = 5;
# - valor > 100 → frete = 0.
# Mostre o valor da compra, o frete e o total a pagar (compra + frete).

valor = float(input("Insira um valor de uma compra: "))

if valor <= 50:
    frete = 10
    print(f"O frete vai ser de {frete}, totalizando R${frete + valor}")
elif valor > 50 and valor < 100:
    frete = 5
    print(f"O frete vai ser de {frete}, totalizando R${frete + valor}")
else:
    frete = 0
    print(f"O frete vai ser de {frete}, totalizando R${frete + valor}")
