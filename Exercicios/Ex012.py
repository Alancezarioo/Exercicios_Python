n1 = float(input("Qual É O Preço Do Produto? R$:"))
n2 = n1 - (n1*5/100)
print("O Seu Produto Que Custava R${}, Na Promoção De 5% De Desconto Ficará R${:.2f}".format(n1,n2))