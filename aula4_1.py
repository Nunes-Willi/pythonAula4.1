from datetime import datetime
import random
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
# frase = input("Digite uma frase: ").lower()

# espacos = frase.count(" ")

# vogais = "aeiou"
# contagem = {vogal: frase.count(vogal) for vogal in vogais}

# print(f"Quantidade de espaços em branco: {espacos}")
# print("Frequência das vogais:")
# for vogal, quantidade in contagem.items():
#     print(f"{vogal}: {quantidade}")

#TODO 8
# frase = input("Digite uma frase: ")
# fraseLimpa = ""

# for c in frase:
#     if c.isalnum():
#         fraseLimpa += c.lower()

# if fraseLimpa == fraseLimpa[::-1]:
#     print("É um palíndromo!")
# else:
#     print("Não é um palíndromo.")

#TODO 9
# cpf = input("Digite o CPF no formato xxx.xxx.xxx-xx: ")
# cpf = cpf.replace(".", "").replace("-", "")

# if cpf.isdigit() and len(cpf) == 11:
#     soma1 = 0
#     for i in range(9):
#         soma1 += int(cpf[i]) * (10 - i)
#     resto1 = (soma1 * 10) % 11
#     if resto1 == 10:
#         resto1 = 0

#     soma2 = 0
#     for i in range(10):
#         soma2 += int(cpf[i]) * (11 - i)
#     resto2 = (soma2 * 10) % 11
#     if resto2 == 10:
#         resto2 = 0

#     if cpf[-2:] == str(resto1) + str(resto2):
#         print("CPF válido!")
#     else:
#         print("CPF inválido!")
# else:
#     print("CPF inválido!")
#TODO 10
# und = ["zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
# dez = ["dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]
# dezenasDez = ["", "", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]

# numero = int(input("Digite um número entre 0 e 99: "))

# if numero >= 0 and numero <= 9:
#     print und[numero])
# elif numero >= 10 and numero <= 19:
#     print(dez[numero - 10])
# elif numero >= 20 and numero <= 99:
#     dez = numero // 10
#     uni = numero % 10
#     if uni == 0:
#         print(dezenasDez[dez])
#     else:
#         print(dezenasDez[dez] + " e " + und[uni])
# else:
#     print("Número fora do intervalo.")

#TODO 11
# palavras = ["banana", "python", "cadeira", "computador", "forca"]
# palavra = random.choice(palavras).upper()
# tentativas = 6
# letrasDescobertas = ["_" for _ in palavra]
# erros = 0

# while erros < tentativas and "_" in letrasDescobertas:
#     print("A palavra é:", " ".join(letrasDescobertas))
#     letra = input("Digite uma letra: ").upper()

#     if letra in palavra:
#         for i in range(len(palavra)):
#             if palavra[i] == letra:
#                 letrasDescobertas[i] = letra
#     else:
#         erros += 1
#         print(f"-> Você errou pela {erros}ª vez. Tente de novo!")

# if "_" not in letrasDescobertas:
#     print("Parabéns! Você acertou:", palavra)
# else:
#     print("Você perdeu! A palavra era:", palavra)

#TODO 12
# telefone = input("Digite o número de telefone (sem espaços ou traços): ")

# if len(telefone) == 7:
#     print("Telefone possui 7 dígitos. Vou acrescentar o dígito três na frente.")
#     telefone = "3" + telefone

# print("Telefone corrigido sem formatação:", telefone)
# print("Telefone corrigido com formatação:", telefone[:4] + "-" + telefone[4:])


#TODO 13
# palavras = ["banana", "computador", "elefante", "brasil", "cachorro", "telefone"]

# palavra_correta = random.choice(palavras).lower()

# letras = list(palavra_correta)
# random.shuffle(letras)
# palavra_embaralhada = ''.join(letras)

# print("Bem-vindo ao Jogo da Palavra Embaralhada!")
# print(f"Adivinhe a palavra: {palavra_embaralhada}")

# tentativas = 6
# acertou = False

# for i in range(1, tentativas + 1):
#     palpite = input(f"Tentativa {i}/{tentativas}: ").strip().lower()
#     if palpite == palavra_correta:
#         print("Parabéns! Você acertou a palavra!")
#         acertou = True
#         break

# if not acertou:
#     print(f"Que pena! Você perdeu. A palavra correta era: {palavra_correta}")
