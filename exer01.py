# Exercício 1 – Quem é mais velho?
# Peça ao usuário:
# - nome1 e idade1;
# - nome2 e idade2.
# Depois, mostre na tela:
# - "[nome1] é mais velho(a)." ou
# - "[nome2] é mais velho(a)." ou
# - "Os dois têm a mesma idade." (se as idades forem iguais).

nome1 = input("Digite seu nome: ")
idade1 = int(input("Digite sua idade: "))

print("\nSegundo nome")
nome2 = input("Digite seu nome: ")
idade2 = int(input("Digite sua idade: "))

if (idade1 > idade2):
    print(f"{nome1} é mais velho que {nome2}")
elif (idade1 < idade2):
    print(f"{nome2} é mais velho que {nome1}")
else:
    print("Os dois tem a mesma idade")
