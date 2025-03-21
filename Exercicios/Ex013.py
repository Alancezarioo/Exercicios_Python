n1 = float(input("Qual É O Salario Do Funcionario? R$:"))
n2 = n1 + (n1*15/100)
print("Um Funcionario Que Ganhava R${}, Com 15% De Aumento, Passa A Receber R${:.2f}".format(n1,n2))