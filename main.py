import sys
class Node:
    def _init_(self, value: int):
        self.value: int = value
        self.next: Node | None = None

def main():
    a = Node(17)
    b = Node(20)
    c = Node(28)
    # en lugar de id tmb se puede usar hex y nos da la dirección en hexadecimal, creo así dijó el ing. pero no me funcionó, verificar esto
    #print(id(a))
    #print(id(b))
    #print(id(c))

    first = a
    a.next = b
    b.next = c
    last = c
    last.value = 20
    print('Primero: ', first)
    print('Segundo: ', a.next)
    print('Tercero: ', a.next.next)
    print('Último: ', last)
    print('Valor en C: ', c.value)

main()
