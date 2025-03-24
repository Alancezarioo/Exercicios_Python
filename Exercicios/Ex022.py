#Crie um programa que leia o nome completo de uma pessoa e mostre: 
#O nome com todas as letras maiúsculas e minúsculas.
#Quantas letras ao todo (sem considerar espaços).
#Quantas letras tem o primeiro nome.

nome = str(input("Digite Seu Nome:")).strip()

print("Seu Nome Em maiúsculas É {}:".format(nome.upper()))

print("Seu Nome Em Minuculas É: {}".format(nome.lower()))

print("Seu Nome Ao Todo Tem: {}" .format(len(nome) - nome.count(' ')))

P = nome.split()

print("Seu Primeiro Nome é {} E Ele Tem Letras {}.".format(P[0],len(P[0])))