# Exercício 6 – Perfil de maratona
# Peça o nome do usuário e quantos episódios ele viu hoje.
# Mostre:
# - 0 episódios → "Hoje você não assistiu nada, [nome].";
# - 1 a 3 → "Assistiu pouco hoje, [nome].";
# - 4 a 8 → "Boa maratona, [nome]!";
# - mais de 8 → "Cuidado para não virar a noite, [nome]!".

nome = input("Qual seu nome?: ")
eps = int(input("Quantos eps você viu hoje?: "))

if eps == 0:
    print(f"Você não assistiu nada {nome}")
elif (eps >= 1 and eps <= 3):
    print(f"Você assistiu pouco {nome}")
elif (eps >= 4 and eps <= 8):
    print(f"Boa maratona {nome}!")
else:
    print(f"Cuidado para não madrugar!")