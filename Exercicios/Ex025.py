#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input("Digite Seu Nome:")).strip()

print("Seu Nome Tem Silva? : {}".format('SILVA' in nome.upper()))