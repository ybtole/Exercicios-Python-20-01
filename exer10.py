# Exercício 10 – Classificação de fase da vida
# Peça a idade do usuário e classifique:
# - 0 a 12 → "Criança";
# - 13 a 17 → "Adolescente";
# - 18 a 59 → "Adulto";
# - 60 ou mais → "Idoso".
# Mostre a idade e a classificação.

idade = int(input("Insira Idade: "))

if idade >= 0 and idade <= 12:
    print(f"{idade}, Criança")
elif idade >= 13 and idade <= 17:
    print(f"{idade}, Adolescente")
elif idade >= 18 and idade <= 59:
    print(f"{idade}, Adulto")
elif idade >= 60:
    print(f"{idade}, Idoso")