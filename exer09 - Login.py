# Exercício 9 – Login simples
# Peça:
# - nome de usuário;
# - senha.
# Considere:
# - usuário correto: "admin";
# - senha correta: "1234".
# Mostre:
# - "Login realizado com sucesso." se os dois estiverem certos;
# - "Senha incorreta." se o usuário estiver certo e a senha errada;
# - "Usuário não encontrado." se o usuário estiver errado.

nome = input("Nome de Usuário: ")
senha = int(input("Senha: "))

if nome == "admin" and senha == 1234:
    print("Login realizado!")
elif nome != "admin" and senha != 1234:
    print("Ambos inválidos")
elif nome != "admin":
    print("Usuário não encontrado!")
elif senha != 1234:
    print("Senha inválida")
