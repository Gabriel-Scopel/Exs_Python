#Exercício 1
# Escreva uma função chamada read_file que abre e exibe o conteúdo de um arquivo chamado "poema.txt". Escreva apenas a função.

def read_file():
  arq = open("poema.txt","r" )
  print(arq.read())
  arq.close()


#Exercício 2
#Escreva uma função chamada conta_palavras que conte e exibe e quantidade de palavras contidas em um arquivo chamado "palavras.txt". Entregue apenas a função.

def conta_palavras():
  arq = open("palavras.txt","r" )
  w=arq.read().split()
  print(len(w))
  arq.close()
 
#Exercício 3
#Crie uma função chamada lista_arquivo, que recebe uma lista de palavras, escreve cada uma dessas palavras em um arquivo e exibe o conteúdo do arquivo. Entregue apenas a função.

def lista_arquivo(lista):
  cor = open('cores.txt', 'w')
  
  for i in lista:
    cor.write('%s\n' %i)
  cor.close()
  
  cor = open('cores.txt', 'r')
  print(cor.read())