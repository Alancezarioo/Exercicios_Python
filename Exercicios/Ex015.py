#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

n1 = int(input("Quantos Dias Alugados? "))
n2 = float(input("Quantos KM Rodados? "))
n3 = (n1 * 60) + (n2 * 0.15)
print("O Valor A Pagar É: R%{}".format(n3))