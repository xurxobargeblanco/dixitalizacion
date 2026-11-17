def rexistrarUsuarios():

    cantidade = int(input("Cantos usuarios queres rexistrar? "))

    with open("usuarios.txt", "w") as ficheiro:

        for i in range(cantidade):

            nome = input("Introduce o nome: ")
            correo = input("Introduce o correo: ")

            ficheiro.write(nome + " - " + correo + "\n")


rexistrarUsuarios()