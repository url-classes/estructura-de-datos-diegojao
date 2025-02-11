from nodos import Node
class List[T]:
    def __init__(self):
        self.head: Node | None = None
        self.tail: Node | None = None

    def append(self, value):
        new_node = Node(value)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def show(self):
        aux = self.head
        while aux is not None:
            if isinstance(aux.value, dict):
                print(f"Nombre: {aux.value['nombre']}, Carnet: {aux.value['carnet']}")
            else:
                print(aux.value)
            aux = aux.next

    def remove(self):
        if self.head is None and self.tail is None:
            raise Exception ("La lista está vacía")
        if self.head is self.tail:
            aux = self.head
            self.head = None
            self.tail = None
            return aux.value
        prev: Node | None = None
        aux: Node | None = self.head

        while aux is not None:
            prev = aux
            aux = aux.next
            if aux is self.tail:
                break

        self.tail = prev
        self.tail.next = None
        return aux.value
    def shift(self):
        aux = self.head
        self.head = self.head.next
        aux.next = None
        self.size -= 1

    def is_empty(self):
        return self.head is None and self.tail is None