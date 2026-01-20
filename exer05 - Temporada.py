#Exercício 5 – Situação da temporada
# Peça:
# - nome da série;
# - total de episódios da temporada;
# - quantos episódios a pessoa já assistiu.
# Mostre:
# - "Você ainda nem começou [série]!" se assistidos == 0;
# - "Você está no meio de [série]." se 0 < assistidos < total;
# - "Você terminou [série]!" se assistidos ≥ total.

serie = input("Nome da série: ")
total_ep = int(input("Quantos eps no total?: "))
ep_assistidos = int(input("Quantos eps assistiu?: "))


if (ep_assistidos == 0):
    print(f"Você não começou {serie}")
elif (ep_assistidos >= total_ep/2 and ep_assistidos < total_ep):
    print("Você está no meio da série")
elif (total_ep > ep_assistidos):
    print(f"Você ainda está assistindo a série {serie}")
elif (total_ep == ep_assistidos):
    print(f"Você terminou a série {serie}!")
