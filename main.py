import sys
from list import List
class Node:
    def _init_(self, value: int):
        self.value: int = value
        self.next: Node | None = None

def main():
    numeros = List()
    numeros.append(17)
    numeros.append(13)
    numeros.append(23)

    print("size", numeros.size)
    print("head", numeros.head)
    print("tail", numeros.tail)
    print("Esta vacía", numeros.is_empty())
    print("Elementos")
    numeros.show()
main()
