# Exercício 3 – Classificação de temperatura
# Peça uma temperatura em graus Celsius e mostre:
# - "Está frio.", se a temperatura for menor que 15;
# - "Clima agradável.", se estiver entre 15 e 25 (inclusive);
# - "Está calor.", se for maior que 25.
# Exercício 4 – Média de 3 notas
temp = int(input("Insira a temperatura: "))

if (temp <= 15):
    print("Está frio")
elif (temp > 15 and temp <= 25):
    print("Clima Agradável")
elif (temp > 25):
    print("Está calor")
