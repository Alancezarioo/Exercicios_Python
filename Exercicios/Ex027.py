#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input("Digite Seu Nome Completo: ")).strip()

s = nome.split()

print("Pazer Em Te Conhecer {}".format(nome))

print("Olha Que Legal, Seu Primeiro Nome É {}".format(s[0]))

print("E Seu Ultimo Nome É {}".format(nome[len(nome)-1]))