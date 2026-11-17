import json

tareas = []

cantidade = int(input("Cantas tarefas queres introducir? "))

for i in range(cantidade):

    titulo = input("Introduce o título da tarefa: ")
    estado = input("Introduce o estado da tarefa: ")

    tarefa = {
        "titulo": titulo,
        "estado": estado
    }

    tareas.append(tarefa)


with open("tareas.json", "w") as ficheiro:
    json.dump(tareas, ficheiro, indent=4)

print("Tarefas gardadas correctamente.")