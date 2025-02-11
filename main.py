import sys
from list import  List
class Student:
    def __init__(self, nombre, carnet):
        self.nombre: str = nombre
        self.carnet: int = carnet
def main():
    edad = List()
    edad.append(18)
    edad.append(20)
    edad.append(21)
    edad.append(13)
    edad.append(15)
    print("Lista:")
    edad.show()
    print("Remuevo el ultimo elemento")
    edad.remove()
    edad.show()
    print("Remuevo el ultimo elemento")
    edad.remove()
    edad.show()
    print("Remuevo el ultimo elemento")
    edad.remove()
    edad.show()
    print("Remuevo el ultimo elemento")
    edad.remove()
    edad.show()
    print("Remuevo el ultimo elemento")
    edad.remove()
    edad.show()
    print("Remuevo el ultimo elemento")
    edad.remove()
    edad.show()
main()