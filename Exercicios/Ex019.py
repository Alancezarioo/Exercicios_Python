import random

n1 = str(input("Nome Do Primeiro Aluno:"))
n2 = str(input("Nome Do Segundo Aluno:"))
n3 = str(input("Nome Do Terceiro Aluno:"))
n4 = str(input("Nome Do Quarto Aluno:"))

lista = [n1,n2,n3,n4]

r = random.choice(lista)

print("O Aluno Escolhido Foi {}".format(r))