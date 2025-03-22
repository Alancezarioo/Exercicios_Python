#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

import math
co = float(input("comprimento do cateto oposto:"))
ca = float(input("comprimento do cateto adiacente:"))
hi = math.hypot(co,ca)
print("O valor da hipotenusa é: {:.2f}".format(hi))