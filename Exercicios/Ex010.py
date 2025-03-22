#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

n1 = float(input("Quantos De Dinheiro Voce Tem Na Carteira? R$:"))
n2 = n1 / 5.70
print("Com R${} Você Pode Comprar US${:.2f}".format(n1,n2))