#O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

n1 = str(input("Nome Do Primeiro Aluno:"))
n2 = str(input("Nome Do Segundo Aluno:"))
n3 = str(input("Nome Do Terceiro Aluno:"))
n4 = str(input("Nome Do Quarto Aluno:"))

listt = [n1,n2,n3,n4]

r = random.shuffle (listt)

print("A Ordem De Apresentação Sera?")
print(listt)