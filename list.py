from nodos import Node
class List:
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


    def is_empty(self):
        return self.head is None and self.tail is None