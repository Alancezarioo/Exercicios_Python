n1 = int(input("Quantos Dias Alugados? "))
n2 = float(input("Quantos KM Rodados? "))
n3 = (n1 * 60) + (n2 * 0.15)
print("O Valor A Pagar É: R%{}".format(n3))