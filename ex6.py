#Exercício 1
#Escreva uma função que tenha os comprimentos dos dois lados mais curtos de um triângulo retângulo como seus parâmetros. Retorne a hipotenusa do triângulo, calculada usando o teorema de Pitágoras, como o resultado da função. Inclua um programa principal que lê os comprimentos dos lados mais curtos de um triângulo retângulo do usuário e use sua função para calcular o comprimento da hipotenusa. Exiba o resultado.

from math import *
cat1 = float(input('digite o cateto 1: '))
cat2 = float(input('digite o cateto 2: '))

def triangulo(cat1, cat2):
  return sqrt(cat1**2+cat2**2)

triangulo(cat1, cat2)

#Exercício 2
#Escreva a função media() que recebe três números como parâmetros e retorna o valor médio desses parâmetros como seu resultado. Escreva somente a função solicitada; não é necessário o programa principal.

def media(a, b, c):
    return(a+b+c)/3

#Exercício 3
#Crie uma função que recebe de 3 a 6 parâmetros e retorna o produto entre eles

def prod(a,b,c,d=1,e=1,f=1):
    return a*b*c*d*e*f

#Exercício 4:
#Em uma determinada jurisdição, as tarifas de táxi consistem em uma tarifa básica de R$ 10.00, mais R$ 0.50 para cada 125 metros percorridos. Escreva uma função que considere a distância percorrida (em quilômetros inteiros) como seu único parâmetro e retorne a tarifa total como seu único resultado. Escreva um programa principal em que a quantidade de km será digitada e onde a função será chamada.

a = int(input('Digite a quantidade de km: '))

def calc(a):
    return (10+4*a)

#Exercício 5:
#Crie uma função para calcular e retornar o peso de uma pessoa nos outros planetas do Sistema Solar. A função deve ter dois parâmetros: o planeta desejado e o peso em Kg da pessoa na Terra. O programa principal deve receber o peso da pessoa na Terra (em Kg) e o planeta desejado.
#Relação de pesos: 1 Kg na Terra equivale a: 0.37 Kg em Mercúrio; 0.88 Kg em Vênus; 0.38 Kg em Marte; 2.64 Kg em Júpiter; 1.15 Kg em Saturno; 1.17 Kg em Urano; e 1.18 Kg em Netuno.  

a = input("Digite o o nome do planeta desejado: ")
b = float(input("Digite o peso da pessoa na Terra em kg: "))

if a == "Mercúrio":
    def pesomercurio(b):
        return b*0.37
    print("Peso em Mercúrio: %.2f" % pesomercurio(b))
elif a == "Vênus":
    def pesoVenus(b):
        return b*0.88
    print("Peso em Vênus: %.2f" % pesoVenus(b))
elif a == "Marte":
    def pesoMarte(b):
        return b*0.38
    print("Peso em Marte: %.2f" % pesoMarte(b))
elif a == "Júpiter":
    def pesoJupiter(b):
        return b*2.64
    print("Peso em Júpiter: %.2f" % pesoJupiter(b))
elif a == "Saturno":
    def pesoSaturno(b):
        return b*1.15
    print("Peso em Saturno: %.2f" % pesoSaturno(b))
elif a == "Urano":
    def pesoUrano(b):
        return b*1.17
    print("Peso em Urano: %.2f" % pesoUrano(b))
elif a == "Neturno":
    def pesoNetuno(b):
        return b*1.18
    print("Peso em Netuno: %.2f" % pesoNetuno(b))

#Exercício 6:
#Escreva uma função, test_prime() que recebe um número e verifica se ele é primo ou não. A função retorna True ou False. Não é necessário desenvolver o programa principal.

def test_prime(num):
    cont = 0
    i = 0
    while i <= num or cont < 2:
        i = i + 1
        x = num % i
        if x == 0:
            cont = cont + 1
    if cont <= 2:
        return True
    else:
        return False

