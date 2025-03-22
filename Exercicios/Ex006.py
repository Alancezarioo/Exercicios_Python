#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n1 = int(input("Digite Um Numero:"))
n2 = n1 * 2
n3 = n1 * 3
Rz = n1 ** (1/2)
print("O dobro De {} vale {}".format(n1,n2))
print("O Triplo De {} vale {}".format(n1,n3))
print("A Raiz Quadrada De {} Vale {:.2f}".format(n1,Rz))