#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

n1 = float(input("Largura Da Parede:"))
n2 = float(input("Altura Da Parede:"))
n3 = n1 * n2
n4 = (n1 * n2) / 2

print("Sua Parede Tem {}X{} E Sua Area É De {}M².".format(n1,n2,n3))
print("Para Pintar Essa Parede, Você Precisara De {}L De Tinta.".format(n4))

