agenda = {
    "Contacto1": 123453333,
    "Contacto2": 666666666,
    "Contacto3": 444444444
}

agendaInversa = {}

for clave, valor in agenda.items():
    agendaInversa[valor] = clave

print(agendaInversa)