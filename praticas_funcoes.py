#Prática Funções:

#Três formas de mostrar o nome e o sobrenome do usuário usando função

# def minha_funcao(nome, sobrenome):
#     print("Prazer", nome, sobrenome + ".")

# nome = input("Digite seu nome: ")
# sobrenome = input("Digite seu sobrenome: ")    

#nome e sobrenome (nesse caso) são variáveis globais, portanto podem ser usadas dentro de funções.

# minha_funcao(nome, sobrenome)



# def minha_funcao():
#     print("Prazer", nome, sobrenome + ".")

# nome = input("Digite seu nome: ")
# sobrenome = input("Digite seu sobrenome: ")
# minha_funcao()



# def minha_funcao(nome, sobrenome):
#     print("Prazer", nome, sobrenome + ".")

# minha_funcao(nome = input("Digite seu nome: "), sobrenome = input("Digite seu sobrenome: "))

#----------------------------------------------------------------------------------------------------------------------------

#Somando valores utilizando função

# def somar(numero_1, numero_2):
#     soma = numero_1 + numero_2
#     print(f"A soma entre {numero_1} e {numero_2} é igual a {soma}.")

# somar(42, 60)

#ou

# def somar(n1, n2):
#     soma = n1 + n2
#     return soma

# resultado_da_soma = somar(4, 5)
# print(f"O resultado da primeira soma é igual a {resultado_da_soma}")

# resultado_de_outra_soma = somar(10, 20)
# print(f"O resultado da segunda soma é igual a {resultado_de_outra_soma}")

#----------------------------------------------------------------------------------------------------------------------------

# def verific_par(numero):
#     if numero % 2 == 0:
#         return True
#     else:
#         return False
    
# if verific_par(17):
#     print("É par!")
# else:
#     print("É ímpar!")


# def verific_nome(nome):
#     if len(nome) > 3:
#         return True
#     else:
#         return False
    
# if verific_nome("Ca"):
#     print("Seu número tem mais que 3 caracteres!")
# else:
#     print("Seu nome tem menos que 3 caracteres!")


# def somar(n1, n2):
#     soma = n1 + n2
#     return soma

# resultado = somar(3, 4)
# print(f"O resultado da soma é igual a {resultado}")


# def somar_lista(*numeros):
#     soma = 0 
#     for n in numeros:
#         soma += n
#     return soma

# soma_dos_numeros_da_lista = somar_lista(6, 5, 4, 3, 2, 1)
# print(f"A soma de todos os números da lista é igual a", soma_dos_numeros_da_lista)

# def calcular_media(*numeros):
#     soma = 0
#     quantidade = len(numeros)

#     for n in numeros:
#         soma += n
#     media = soma / quantidade
#     return media

# resultado = calcular_media(2, 4, 5, 11, 3)
# print(resultado)

#Exercícios
# def maior_num(*numero):
