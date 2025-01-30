from nodos import Node
class List:
    def __init__(self):
        self.size = 0
        self.head: Node | None  = None
        self.tail: Node | None  = None

    def append(self, value: int):
        new_node = Node(value)

        if self.is_empty():
            self.head =new_node
            self.tail = new_node
            self.size += 1
        else:
            self.tail.next = new_node
            self.tail   = new_node
            self.size += 1

    def show(self):
        aux = self.head

        while aux is not None:
            print(aux.value)
            aux = aux.next


    def is_empty(self):
        return self.head is None and self.tail is None