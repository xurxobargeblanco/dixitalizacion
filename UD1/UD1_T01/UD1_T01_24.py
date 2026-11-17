import json

with open("tareas.json", "r") as ficheiro:
    tareas = json.load(ficheiro)


for tarefa in tareas:

    if tarefa["estado"] == "pendiente":

        print("Tarefa:", tarefa["titulo"])
        print("Estado:", tarefa["estado"])
        print("-------------------")