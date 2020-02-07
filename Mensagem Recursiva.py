# Mostrar uma mensagem a partir de um código recursivo

# Nome do projeto: Mensagem Recursiva
# Linguagem: Python
# Utilizações: Variáveis, Listas e Funções(Recursividade)
# Autor: Rafael Lua - rafaellua13



def mensagem(vetor,cont):

  print(vetor[cont],end="")
  
  if vetor[cont] == ":)":
    return 0

  cont += 2
  mensagem(vetor,cont)
  

cont = 0
vetor = ["H","1","e","2","l","3","l","4","o","5"," ","6","M","7","u","8","n","9","d","10","o","11"," ","12",":)"]


mensagem(vetor,cont)

