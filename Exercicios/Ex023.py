##Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

numero = int(input("Informe Um Numero: "))

n1 = str(numero)

print("Unidade: {}".format(n1[3]))
print("Dezena: {}".format(n1[2]))
print("Centena: {}".format(n1[1]))
print("Milhar: {}".format(n1[0]))