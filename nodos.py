class Node[T]:
    def __init__(self, value):
        self.value = value
        self.next: Node | None = None
    def __str__(self):
        return str(self.value)