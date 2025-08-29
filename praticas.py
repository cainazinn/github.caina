# Hoje criaremos uma estrutura de repetição, mais conhecido como Loop, usando Python
# v = 1
# while v <= 100:
    # print("Este loop está sendo executado pela", str(v) + "°", "vez.")
    # v += 1

# for v in range(0, 101, 2):
#    print(v)

# frutas = ["Banana", "Maçã", "Pera", "Laranja"]
# for f in frutas:
#     print(f)

# nome = input("Digite o nome de qualquer coisa: ")
# nome = nome.upper()

# for letra in nome:
#     if letra == "A":
#         continue
#     elif letra == "E":
#         continue
#     elif letra == "I":
#         continue
#     elif letra == "O":
#         continue
#     elif letra == "U":
#         continue
#     print(letra)

# números = [1, 2, 4, 7, 10, 11]
# for n in números:
#     if n % 2 != 0:
#         continue
#     print("O número", n, "é par!")

# número = 1
# while número <= 10:
#     print(número)
#     número += 1

# for número in range(1, 11):
#     print(número)

# número = int(input("Digite um número: "))
# for n in range(1, número + 1):
#     print(número * n)

# palavra = input("Digite uma palavra: ")
# palavra.upper()

# for letra in palavra:
#     if letra != "A":
#         continue
#     elif letra != "E":
#         continue
#     elif letra != "I":
#         continue
#     elif letra != "O":
#         continue
#     elif letra != "U":
#         continue
#     print(letra)


# Exemplo 1: 
# Peça ao usuário que digite uma nota de 0 a 10 e se o usuário fornecer uma nota menor do que 0 ou maior do que 10, faça com que apaeça uma mensagem de erro e peça que ele digite uma nota de novo até que esteja entre 0 ou 10.

# nota = float(input("Digite uma nota de 0 a 10: "))

# while nota > 10 or nota < 0:

#     print("Nota inválida, tente novamente!")
#     nota = float(input("Digite uma nota de 0 a 10: "))

# print("Nota válida!", "A nota escolhida foi", nota)


# Exemplo 2: 
# Peça ao usuário o seu nome e sua senha, se a senha for igual ao nome, não aceite e peça que o usuário insira uma senha válida, ou seja, diferente de seu nome.

# nome = input("Digite seu nome de usuário: ")
# senha = input("Digite uma senha: ")

# while senha == nome:

#     print("ERRO! A senha não pode ser igual ao nome de usuário!")
#     senha = input("Digite sua senha: ")

# print("Cadastro realizado com sucesso!")

# Exemplo 3: 
# Faça um programa que valide informações, se as informações não forem válidas peça ao usuário que as reescreva até que as informações sejam válidas.

nome = input("Digite seu nome (mínimo 3 caracteres): ")
idade = int(input("Digite sua idade: "))
sexo = input("Digite seu sexo ('f' para feminino e 'm' para masculino): ")
salario = float(input("Digite quanto você ganha por mês: "))
estado_civil = input("Digite seu estado_civil ('s', 'c' ou 'd'): ")

while len(nome) < 3:
    print("É necessário que seu nome tenha pelo menos 3 caracteres")
    nome = input("Digite seu nome (mínimo 3 caracteres): ")

while idade < 0 or idade > 150:
    print("Idade inválida!")
    idade = input("Digite sua idade: ")

while sexo != "f" and sexo != "m":
    print("Biologicamente você deve ser do sexo masculino ou feminino!")
    sexo = input("Digite seu sexo: ")

while salario <= 0:
    print("Você deve ganhar ao menos 1 real por mês!")
    salario = float(input("Digite quanto você ganha por mês: "))

print("Cadastro realizado com sucesso!")
