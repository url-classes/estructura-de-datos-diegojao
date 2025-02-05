import sys
from list import  List
def main():
    edad = List()
    edad.append(18)
    edad.append(20)
    edad.append(21)
    edad.append(13)
    edad.append(15)
    print('Edades: ')
    edad.show()

    nombres = List()
    nombres.append('Diego')
    nombres.append('Jose')
    nombres.append('Alegria')
    nombres.append('Oros')
    nombres.append('Jao')
    print('Nombres: ')
    nombres.show()

    nota = List()
    nota.append(98)
    nota.append(65)
    nota.append(43)
    nota.append(87)
    nota.append(100)
    print('Notas: ')
    nota.show()

    estudiante = List()
    estudiante.append({'nombre': 'Diego', 'carnet': 1631524})
    estudiante.append({'nombre': 'José', 'carnet': 1631525})
    estudiante.append({'nombre': 'Alegría', 'carnet': 1631526})
    estudiante.append({'nombre': 'Orós', 'carnet': 1631527})
    estudiante.append({'nombre': 'Jao', 'carnet': 1631528})

    print('Estudiantes: ')
    estudiante.show()

main()