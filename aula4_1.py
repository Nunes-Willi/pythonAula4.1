from datetime import datetime
#TODO 01
# a = input("Escreva um texto: ")
# b = input("Escreva outro: ")

# if len(a) == len(b)  and str(a) == str(b):
#     print(f"As duas strings tem o mesmo conteúdo e comprimento: \n a = {a , len(a)} b = {b , len(b)}")
# elif len(a) == len(b)  and str(a) != str(b):
#     print(f"As duas strings tem o mesmo comprimento, conteúdos diferentes: \n a = {a , len(a)} b = {b , len(b)}")
# else:
#     print(f"Comprimentos diferentes: \n a = {a , len(a)} b = {b , len(b)}")

#TODO 02
# nome = input("Escreva seu nome: ")

# nome = nome.upper()[::-1]
# print(nome)

#TODO 03
# nome = input("Escreva seu nome: ")

# for i in range(len(nome)):
#     print(nome[i])

#TODO 04
# nome = input("Escreva seu nome: ")

# for i in range(1, len(nome) + 1):
#     print(nome[:i])

#TODO 05
# nome = input("Escreva seu nome: ")

# for i in range(len(nome) + 1):
#     print(nome[i:])

#TODO 06
# nome = input("Escreva seu nome: ")
# nascd = input("Digite sua data de nascimento (dd/mm/aaaa): ")
# dataFormat = datetime.strptime(nascd, "%d/%m/%Y")
# meses = [
#     "janeiro", "fevereiro", "março", "abril", "maio", "junho",
#     "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
# ]
# 2
# mes = meses[dataFormat.month - 1]

# print(f"{nome} nasceu em {dataFormat.day} de {mes} de {dataFormat.year}.")

#TODO 07
frase = input("Digite uma frase: ").lower()

espacos = frase.count(" ")

vogais = "aeiou"
contagem = {vogal: frase.count(vogal) for vogal in vogais}

print(f"Quantidade de espaços em branco: {espacos}")
print("Frequência das vogais:")
for vogal, quantidade in contagem.items():
    print(f"{vogal}: {quantidade}")