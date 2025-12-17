def menu():
    print("""
  *-*-*-*- MENU -*-*-*-*
*                        *
*   1 - Criar            *
*   2 - Listar           *
*   3 - Deletar          *
*   4 - Sair             *
*                        *
  -*-*-*-*-*-*-*-*-*-*-*-
""")

def criar_tarefa():
    tarefa = input("Digite sua tarefa abaixo:\n").split()
    lista_de_tarefas.append(tarefa)

def listar_tarefas(lista):
    if lista_de_tarefas == "":
      print("Lista Vazia.")
    else:
      print("To-Do List:")
      for id,tarefa in enumerate(lista, start=1):
        print(f"{id} - {tarefa}")

def deletar_tarefa(lista):
    if lista == "":
       print("Lista Vazia.")
    else:   
      listar_tarefas(lista)
      deletar = int(input("selecione a tarefa que você deseja deletar ou zero para cancelar a operação: "))
      if len(lista) >= deletar >= 1:
         lista.pop(deletar-1)
      else:
         print("Fora de alcance.")
         
       
#===================================================================#


lista_de_tarefas = list()

while True:
  menu()
  seletor = int(input("--> "))
  if seletor == 1:
      criar_tarefa()
  elif seletor == 2:
      listar_tarefas(lista_de_tarefas)
  elif seletor == 3:
      deletar_tarefa(lista_de_tarefas)
  elif seletor == 4:
      print("Fim")
      break    