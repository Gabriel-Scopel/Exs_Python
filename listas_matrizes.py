#Exercícío 1
# Faça um programa que preencha uma matriz M (2x2), solicitando cada elemento (números inteiros) para o usuário. Depois, calcule e mostre uma matriz resultante da multiplicação dos elementos de M pelo seu maior elemento. Utilize %3d para imprimir a matriz.

a=[]
c =[]
maior = 0
for i in range(2):
  b=[]
  for i in range(2):
     b.append(int(input("Digite um valor: ")))
  a.append(b)

for i in a:
  for j in i:
    if j>maior:
      maior=j

for i in a:
  x=[]
  for j in i:
    x.append(j*maior)
  c.append(x)

for i in c:
  for j in i:
    print("%3d" %j, end=" ")
  print()

#Exercício 2
## Faça um programa que preencha:
# Uma lista com 3 nomes de lojas
# Uma outra lista com 5 nomes de produtos
# Uma matriz com os preços de todos os produtos em cada loja
# O programa deverá mostrar todas as listas: lojas, produtos e preços(Utilize % 3d para imprimir a matriz). Depois, deverá mostrar todas relações(nome do produto – nome da loja - preço) em que o preço não ultrapasse R$ 50, 00.

